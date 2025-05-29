from rest_framework.viewsets import ModelViewSet
from dev_core.security.mix_authentication import MIX_AUTHEN_TSJ
from dev_core.security.mix_permission import (
    MIX_PERMISSION_ADMIN,
    MIX_PERMISSION_AUTH,
    MIX_PERMISSION_ANY
)
from dev_core.settings.base.drf.pagin_drf import CustomPagination
from dev_core.security.middleware.throttling.base_throttling import (
    UNTHENTHROTTLE,
    AUTHENTHROTTLE,
    generate_throttle_classes
)
from rest_framework.response import Response
from dev_core.security.export import cache_decorator_factory_anhtudev 

class BaseStrictModelViewSet(ModelViewSet): #* Custom ModelViewSet
    '''
        Base Strict Router
            - Purpose: CRUD
            - Permission: IsAuthenticated
            - Authentication: JWT, Token, Session

        Mục đích chính hạn chế quyền truy cập của người dùng khi chưa đăng nhập, chặn tất cả các phương thức khi bị tấn công DDOS
    '''
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    #* Cache the response for 15 minutes
    cache_response = 60 * 15 #* if =0 => no cache

    @cache_decorator_factory_anhtudev.create_cache_decorator(timeout=cache_response)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @cache_decorator_factory_anhtudev.create_cache_decorator(timeout=cache_response)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @cache_decorator_factory_anhtudev.create_cache_decorator(timeout=cache_response)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @cache_decorator_factory_anhtudev.create_cache_decorator(timeout=cache_response)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @cache_decorator_factory_anhtudev.create_cache_decorator(timeout=cache_response)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @cache_decorator_factory_anhtudev.create_cache_decorator(timeout=cache_response)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
   
    def get_permissions(self):
        if self.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = MIX_PERMISSION_ADMIN
        elif self.action in ['retrieve']:
            self.permission_classes = MIX_PERMISSION_ANY
        return [permission() for permission in self.permission_classes]

    def get_throttles(self):
        if self.request.method == 'GET':
            self.throttle_classes = UNTHENTHROTTLE['GET']
        elif self.request.method in 'POST':
            self.throttle_classes = UNTHENTHROTTLE['POST']
        elif self.request.method in 'PUT':
            self.throttle_classes = UNTHENTHROTTLE['PUT']
        elif self.request.method in 'PATCH':
            self.throttle_classes = UNTHENTHROTTLE['PATCH']
        elif self.request.method in 'DELETE':
            self.throttle_classes = UNTHENTHROTTLE['DELETE']
        return [throttle() for throttle in self.throttle_classes]
    


class AuthenStrictModelViewSet(BaseStrictModelViewSet):
    '''
        Authen Strict Router
            - Purpose: CRUD
            - Permission: IsAuthenticated
            - Authentication: JWT, Token, Session
    '''
    def get_permissions(self): #* Only authen is allowed
        return [permission() for permission in MIX_PERMISSION_AUTH]
    

    def get_throttles(self):
        if self.request.method == 'GET':
            self.throttle_classes = AUTHENTHROTTLE['GET']
        elif self.request.method in 'POST':
            self.throttle_classes = AUTHENTHROTTLE['POST']
        elif self.request.method in 'PUT':
            self.throttle_classes = AUTHENTHROTTLE['PUT']
        elif self.request.method in 'PATCH':
            self.throttle_classes = AUTHENTHROTTLE['PATCH']
        elif self.request.method in 'DELETE':
            self.throttle_classes = AUTHENTHROTTLE['DELETE']
        return [throttle() for throttle in self.throttle_classes]



class UnauthenStrictModelViewSet(BaseStrictModelViewSet):
    ...
    


class AdminStrictModelViewSet(BaseStrictModelViewSet):
    def get_permissions(self): #* Only admin is allowed
        return [permission() for permission in MIX_PERMISSION_ADMIN]
    
    def get_throttles(self):
        return [throttle() for throttle in generate_throttle_classes(authen=True, http_method_names=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'], throttle_scope='admin', throttle_rate=2000, time_period='d')]




    