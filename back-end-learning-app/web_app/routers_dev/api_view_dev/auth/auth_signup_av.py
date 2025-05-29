from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from web_app.serializers import UserSerializer
from web_app.models import User, Userrole, Role
from utils.export import ResUtil
from dev_core.security.export import *
from rest_framework.exceptions import APIException
from django.db.models import Q



class AuthSignUpAV(APIView):
    '''
        Sign up API View
            - Purpose: Sign up to create user
            - Request: POST
                - username: string
                - email: string
                - password: string
                - full_name: string
                - phone: string (optional)
            - Permission: AllowAny
    '''
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    http_method_names=['post']
    name_api = 'Sign Up API'


    def post(self, request):
        try:
            # Validate request data
            serializer = UserSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(ResUtil.res_fail(
                    name_res=self.name_api,
                    data={
                        'status': 400,
                        'message': 'Invalid input data',
                        'errors': serializer.errors
                    }
                ), status=status.HTTP_400_BAD_REQUEST)

            # Create user
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()

            # Create user role (case-insensitive lookup)
            get_role = Role.objects.filter(Q(role_name__iexact='student')).first()
            if not get_role:
                get_role = Role.objects.create(role_name='Student')
                get_role.save()

            userrole = Userrole.objects.create(user=user, role=get_role)
            userrole.save()

            # Return success response
            return Response(ResUtil.res_success(
                name_res=self.name_api,
                data={
                    'username': user.username,
                    'email': user.email,
                    'full_name': user.full_name,
                    'phone': user.phone,
                    'created_at': user.created_at,
                    'updated_at': user.updated_at,
                }
            ), status=status.HTTP_200_OK)

        except Exception as e:
            # Log the error for debugging
            print(f"Signup error: {str(e)}")
            return Response(ResUtil.res_fail(
                name_res=self.name_api,
                data={
                    'status': 500,
                    'message': 'An error occurred during signup',
                    'error': str(e)
                }
            ), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = MIX_PERMISSION_ANY
        else:
            self.permission_classes = self.permission_classes
        return [permission() for permission in self.permission_classes]