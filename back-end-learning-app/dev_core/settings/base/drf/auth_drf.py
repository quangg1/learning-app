
from .pagin_drf import CustomPagination
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': CustomPagination,
    #* Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    #* Permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    #* Parser and Renderer settings
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 15, # cache for 15 minutes
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    #* Throttling settings
    #  'DEFAULT_THROTTLE_CLASSES': [
    #      'rest_framework.throttling.ScopedRateThrottle',
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle',
    #     'dev_core.security.export.GetAnonRateThrottle',
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'get_anon': '10/day',
    #     'anon': '5/day',
    #     'user': '5/day',
    # }
}