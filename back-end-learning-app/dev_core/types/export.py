'''
This file is used to export all the types that are used in the dev_core package.
'''
from dev_core.types.base_type import *

#* ModelViewSet is http_method_names is lowercase
HTTP_METHOD_NAME_TYPE = Literal['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS', 'TRACE', 'CONNECT', 'get', 'post', 'put', 'delete', 'patch', 'head', 'options', 'trace', 'connect']


KEY_TYPE = Literal['GOOGLE_ID', 'GOOGLE_SECRET', 'SECRET_KEY', 'DEBUG', 'API_ROUTE', 'MY_EMAIL', 'MY_EMAIL_PASSWORD', 'HOST_BE_LOCAL', 'HOST_BE_PRODUCTION']