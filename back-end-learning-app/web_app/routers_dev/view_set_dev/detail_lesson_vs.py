from rest_framework.viewsets import ModelViewSet
from web_app.models import Detaillesson, Lesson
from web_app.serializers import DetaillessonSerializer
from dev_core.security.export import *
from utils.export import *
from rest_framework.decorators import action
from rest_framework.response import Response
#* Slugify is used to convert a string to a slug
from django.utils.text import slugify
from django.db.models import Count

#* Cache the response for 15 minutes



class DetailLessonVS(UnauthenStrictModelViewSet):
    #^ ViewSet for Detaillesson model
    '''
        DetailLesson View Set from BaseStrictModelViewSet
            - Purpose: CRUD Detaillesson
            - Permission: IsAuthenticated
            - Authentication: JWT, Token, Session
    '''
    queryset = Detaillesson.objects.all()
    serializer_class = DetaillessonSerializer
    pagination_class = CustomPagination if table_exists_util('detaillesson') and Detaillesson.objects.annotate(id_count=Count('id')).count() > 10 else None

    # Add this method to get the queryset for the Course model
    
    @cache_decorator_factory_anhtudev.create_cache_decorator()
    @action(detail=True, methods=['GET'], url_path='list-detaillesson-of-lesson')
    def list_detaillesson_of_lesson(self, request, pk=None):
        '''
            Get all detaillessons of a lesson
        '''
        paginator = self.pagination_class() if self.pagination_class else None
        try:
            lesson = Lesson.objects.get(pk=pk)
            detaillessons = Detaillesson.objects.select_related('lesson').filter(lesson=lesson).order_by('id') #* Fixxed error UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'web_app.models_dev.Lesson.Lesson'> QuerySet, using order_by('id') to fix it.

            page = paginator.paginate_queryset(detaillessons, request)
            serializer = DetaillessonSerializer(page, many=True)
            data = paginator.get_paginated_response(serializer.data).data
            return Response({
                'links': data['links'],
                'count': data['count'],
                'results': [ 
                    {
                        'id': detaillesson['id'],
                        'name': detaillesson['name'],
                        'extent_name': detaillesson['extent_name'],
                        'updated_at': detaillesson['updated_at'],
                        'slug': slugify(detaillesson['name']) #* Convert the name to a slug
                    } for detaillesson in data['results']
                ]
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def get_permissions(self):
        '''
            Get the permission for the viewset
            .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy()
        '''
        #* Deny the permission for the list action if the user is not an admin
        # # print(self.request.method) #* Custom in UnauthenStrictModelViewSet
        # if self.action == 'list':
        #     self.permission_classes  = MIX_PERMISSION_ADMIN
        if self.action == 'retrieve' or self.action == 'list_detaillesson_of_lesson':
            self.permission_classes  = MIX_PERMISSION_ANY
        return [permission() for permission in self.permission_classes ] #* Default permission from base class