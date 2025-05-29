from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from dev_core.settings.settings import *
from django.http import HttpResponse
from dev_core.settings.settings import ADMIN_TEMPLATES
#* print(API_ROUTE)
#*--------------------------------------------------------------
#** brand_name = 'Group 6: Building website for saling online courses and managing courses'

def index(request):
    return HttpResponse('You are not allowed to access this page.')
#*--------------------------- Error 404 ---------------------------
if ADMIN_TEMPLATES:
    handler404 = 'dev_core.security.provider.handle_404.error_404_view'
#*--------------------------------------------------------------
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', index, name='index'),
]
#*--------------------------------------------------------------
#* Admin
if ADMIN_TEMPLATES:
    from django.contrib import admin
    brand_name = 'Learning App'
    admin.site.site_header = brand_name
    admin.site.site_title = brand_name
    admin.site.index_title = brand_name
    urlpatterns += [
        path('admin/', admin.site.urls, name='admin_login'),
    ]
#*--------------------------------------------------------------
#* Url social login
#* from web_app.social_login.google_api import GoogleLogin

#* urlpatterns += [
#*     path(f'{API_ROUTE}/dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
#*     path(f'{API_ROUTE}/dj-rest-auth/', include('dj_rest_auth.urls')),
#*     path(f'{API_ROUTE}/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  
#* ]
#*--------------------------------------------------------------
#* API View
from web_app.routers import (
    AuthSignInAV, 
    AuthSignUpAV, 
    AuthTokenAV,
    SubmissionAV,
    CommonAV
)

urlpatterns += [
    path(f'{API_ROUTE}/api-view/sign-up/', AuthSignUpAV.as_view(), name='auth_login'),
    path(f'{API_ROUTE}/api-view/sign-in/', AuthSignInAV.as_view(), name='auth_signup'),
    path(f'{API_ROUTE}/api-view/token/', AuthTokenAV.as_view(), name='auth_token'),
    path(f'{API_ROUTE}/api-view/submission/', SubmissionAV.as_view(), name='submission'),
    #* API custom decorator for services
    path(f'{API_ROUTE}/api-view/common/contact/', CommonAV.contact, name='contact'),
    path(f'{API_ROUTE}/api-view/common/comment-course/', CommonAV.comment_course, name='comment_course'),
    path(f'{API_ROUTE}/api-view/common/get-all-comment/', CommonAV.get_all_comment, name='get_all_comment'),
    path(f'{API_ROUTE}/api-view/common/get-data-analysis/', CommonAV.get_data_analysis, name='get_data_analysis'),
    path(f'{API_ROUTE}/api-view/common/check-admin/', CommonAV.check_admin, name='check_admin'),
    path(f'{API_ROUTE}/api-view/common/forgot-password/', CommonAV.forgot_password, name='forgot_password'),
]

#*--------------------------------------------------------------
#* Register View Sets
from web_app.routers import router
urlpatterns += router.urls

#*--------------------------------------------------------------
#* JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns += [
    path(f'{API_ROUTE}/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_ROUTE}/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


#* from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#* urlpatterns += staticfiles_urlpatterns()