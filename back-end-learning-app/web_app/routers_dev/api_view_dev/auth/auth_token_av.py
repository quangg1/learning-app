from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from web_app.serializers import UserSerializer
from web_app.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from utils.export import *
from dev_core.security.export import *



class AuthTokenAV(APIView):
    '''
        Sign in API View
            - Purpose: Sign in to authenticate user
            - Request: POST
                - username: string
                - password: string
            - Permission: AllowAny
            - Authentication: None
    '''
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    http_method_names=['post', 'get']
    name_api = 'Token For Sending Email API'
    def post(self, request):
        get_user = User.objects.filter(email=request.data['email']).first()
        # print(request.data['host'])
        try:
            host_fe = request.data['host']
        except:
            host_fe = 'http://localhost:3000'
        if not get_user:
            return Response(ResUtil.res_fail(
                name_res=AuthTokenAV.name_api,
                data={
                    'status': 401,
                    'message': 'Username or password is incorrect!',
                }
            ), status=status.HTTP_401_UNAUTHORIZED)
        
        refresh_token = RefreshToken.for_user(get_user)

        if get_user.is_active:
            send_email_util(
                subject='Đăng Nhập Cùng Learning App!',
                message=f'Cảm ơn bạn đã tham\nĐăng Nhập Bấm Vào Đây: {host_fe}/?authToken={refresh_token.access_token}',
                recipient_list=[get_user.email]
            )
            return Response(ResUtil.res_success(
                name_res=AuthTokenAV.name_api,
                data={
                    'status': 200,
                    'message': 'Email sent successfully!',
                }
            ), status=status.HTTP_200_OK)
        
        return Response(ResUtil.res_fail(
            name_res=AuthTokenAV.name_api,
            data={
                'status': 401,
                'message': 'Your account has been disabled!',
            }
        ), status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request):
        return Response(ResUtil.res_success(
                name_res=AuthTokenAV.name_api,
                data={
                    'status': 200,
                    'message': 'Welcome to Learning App!',
                }
            ), status=status.HTTP_200_OK)

    def get_permissions(self):
        '''
            Get the permission for the viewset
        '''
        if self.request.method == 'POST':
            self.permission_classes = MIX_PERMISSION_ANY
        else:
            self.permission_classes = self.permission_classes
        return [permission() for permission in self.permission_classes]
    
    def get_throttles(self):
        if self.request.method == 'POST':
            self.throttle_classes = generate_throttle_classes(authen=False, 
                                                              time_period='h', 
                                                              throttle_rate=2, 
                                                              throttle_scope='auth_token_api_view')
        return [throttle() for throttle in self.throttle_classes]
        
    