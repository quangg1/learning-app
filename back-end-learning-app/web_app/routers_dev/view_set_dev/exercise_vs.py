from rest_framework.viewsets import ModelViewSet
from web_app.models import Exercise, Tagname
from web_app.serializers import ExerciseSerializer
from dev_core.security.export import *
from utils.export import *
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

class ExerciseVS(UnauthenStrictModelViewSet):
    '''
        User View Set
            - Purpose: CRUD User
            - Permission: IsAuthenticated, IsAdminUser
            - Authentication: JWT, Token, Session
    '''
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    pagination_class = CustomPagination if table_exists_util('exercise') and Exercise.objects.annotate(id_count=Count('id')).count() > 10 else None

    @cache_decorator_factory_anhtudev.create_cache_decorator()
    @action(methods=['GET'], detail=False, url_path='get-exercise-detail')
    def get_exercise_detail(self, request):
        # Add implementation if necessary
        return Response(status=200)

    @cache_decorator_factory_anhtudev.create_cache_decorator()
    @action(methods=['GET'], detail=False, url_path='get-all-exercise-by-name')
    def get_all_exercise_by_name(self, request):
        paginator = self.pagination_class() if self.pagination_class else None
        get_slug_tag_name = request.GET.get('slugTagName')
        try:
            if get_slug_tag_name:
                tag_name = Tagname.objects.prefetch_related('exercises').get(slug_tagname=get_slug_tag_name)
                exercises = tag_name.exercises.all().order_by('id')
            else:
                exercises = Exercise.objects.all().order_by('id')

            if paginator:
                page = paginator.paginate_queryset(exercises, request)
                serializer = ExerciseSerializer(page, many=True)
                data = paginator.get_paginated_response(serializer.data).data
            else:
                serializer = ExerciseSerializer(exercises, many=True)
                data = serializer.data

            return Response({
                'links': data.get('links') if paginator else None,
                'count': data.get('count') if paginator else len(serializer.data),
                'results': [
                    {
                        'id': exercise['id'],
                        'title': exercise['title'],
                        'description': exercise['description'],
                        'detail_lesson': exercise['detail_lesson'],
                        'link_solution': exercise['link_solution'],
                        'code_solution': exercise['code_solution'],
                        'extent': exercise['extent'],
                        'created_at': exercise['created_at'],
                        'updated_at': exercise['updated_at']
                    } for exercise in (data['results'] if paginator else serializer.data)
                ]
            })
        except ObjectDoesNotExist:
            return Response({'error': 'Tagname not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def get_permissions(self):
        if self.action in ['get_all_exercise_by_name', 'get_exercise_detail', 'retrieve']:
            self.permission_classes = MIX_PERMISSION_ANY
        return [permission() for permission in self.permission_classes]
    
    def get_throttles(self):
        if self.request.method == 'GET':
            self.throttle_classes = generate_throttle_classes(
                authen=True,
                http_method_names=['get'],
                throttle_rate=1000,
                time_period='h',
                throttle_scope='get_exercise_detail',
            )
        return [throttle() for throttle in self.throttle_classes]
