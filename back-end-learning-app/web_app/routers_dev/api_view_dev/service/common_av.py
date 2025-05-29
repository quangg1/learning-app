from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    throttle_classes
)
from rest_framework.response import Response
from rest_framework.request import Request
from utils.email_util import send_email_util
from utils.res_util import ResUtil
from dev_core.settings.settings import EMAIL_ADMIN_GROUP
from typing import (
    Literal,
    Optional
)
from dev_core.security.export import (
    #* Permission
    MIX_PERMISSION_ANY,
    MIX_PERMISSION_ADMIN,
    MIX_PERMISSION_AUTH,
    #* Authentication
    MIX_AUTHEN_TSJ,
    #* Throttle 
    UNTHENTHROTTLE,
    AUTHENTHROTTLE,
    generate_throttle_classes
)

HTTP_METHODS = Literal['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS', 'TRACE']

from web_app.models import (
    Course,
    Comment,
    User
)

from web_app.serializers import (
    CourseSerializer,
    CommentSerializer
)

import requests as req

from dev_core.security.export import CustomPagination


def mix_decorators(
        http_methods:Optional[HTTP_METHODS]=['GET'], 
        permissions=None, 
        authentications=None,
        throttles=None
    ):
    def decorator(func):
        # Apply the API view decorator with the specified HTTP methods
        decorated_func = api_view(http_methods)(func)
        
        # Apply the permission classes decorator if any are specified
        if permissions:
            decorated_func = permission_classes(permissions)(decorated_func)
        
        # Apply the authentication classes decorator if any are specified
        if authentications:
            decorated_func = authentication_classes(authentications)(decorated_func)

        # Apply the throttle classes decorator if any are specified
        if throttles:
            decorated_func = throttle_classes(throttles)(decorated_func)

        
        return decorated_func
    return decorator




class CommonAV:

    @staticmethod
    @mix_decorators(http_methods=['POST'])
    def contact(request: Request):
        body = request.data
        send_email_util(
            message='Nội dung: ' + body.get('message'),
            recipient_list=[EMAIL_ADMIN_GROUP],
            subject=body.get('email') + ', Gửi cho bạn 🥰'

        )
        return Response(ResUtil.res_success(
            data=body,
            name_res='contact'
        ))
    
    @staticmethod
    @api_view(['POST'])
    @permission_classes(MIX_PERMISSION_AUTH)
    @authentication_classes(MIX_AUTHEN_TSJ)
    def comment_course(request: Request):
        data = {
            'course': request.data.get('course'),
            'content': request.data.get('content'),
            'user': request.user.id,
            'sentiment': req.post(
                url='https://django-test-sentiment.onrender.com/api/sentiment',
                json={'text': request.data.get('content')}
            ).json().get('res')
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResUtil.res_success(
                data=serializer.data,
                name_res='comment'
            ))
        return Response(ResUtil.res_fail(
            data=serializer.errors,
            name_res='comment'
        ))
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes(MIX_PERMISSION_ANY)
    def get_all_comment(request: Request):
        paginator = CustomPagination() if CustomPagination else None
        comments = Comment.objects.all()
        page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(page, many=True)
        data = paginator.get_paginated_response(serializer.data).data
        return Response(ResUtil.res_success(
            data=data,
            name_res='comments'
        ))
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes(MIX_PERMISSION_ANY)
    def get_data_analysis(request: Request):
        data_courses = Comment.objects.select_related('course').all()
        data_courses = CommentSerializer(data_courses, many=True).data

        data_positive = {
            'total': sum([1 for comment in data_courses if comment.get('sentiment') == 'positive']),
            'label': 'positive'
        }

        data_negative = {
            'total': sum([1 for comment in data_courses if comment.get('sentiment') == 'negative']),
            'label': 'negative'
        }

        data_neutral = {
            'total': sum([1 for comment in data_courses if comment.get('sentiment') == 'neutral']),
            'label': 'neutral'
        }

        return Response(ResUtil.res_success(
            data={
                'data_positive': data_positive,
                'data_negative': data_negative,
                'data_neutral': data_neutral
            },
            name_res='data_analysis'
        ))
    
    @staticmethod
    @api_view(['GET'])
    @permission_classes(MIX_PERMISSION_ADMIN)
    @authentication_classes(MIX_AUTHEN_TSJ)
    def check_admin(request: Request):
        return Response(ResUtil.res_success(
            data={
                'message': 'You are admin'
            },
            name_res='check_admin'
        ))
    

    @staticmethod
    @api_view(['GET'])
    @permission_classes(MIX_PERMISSION_ANY)
    # @throttle_classes(generate_throttle_classes(
    #     authen=False, 
    #     time_period='h', 
    #     throttle_rate=2, 
    #     throttle_scope='forgot_password'))
    def forgot_password(request: Request):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        _random_password = random_password()
        user.set_password(_random_password)
        user.save()
        send_email_util(
            message='Mật khẩu của bạn là: ' + _random_password,
            recipient_list=[email],
            subject='Quên mật khẩu'
        )
        return Response(ResUtil.res_success(
            data={
                'message': 'Check your email'
            },
            name_res='forgot_password'
        ))


def random_password(k=8):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


    