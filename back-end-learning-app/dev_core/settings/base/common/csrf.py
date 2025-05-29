#* #** CSRF settings
from dev_core.settings.settings import *

#*The domain to be used when setting the CSRF cookie. If set . before the domain name, then it also allow for subdomain.
CSRF_COOKIE_SAMESITE = 'Strict' if DEBUG == False else 'Lax'
#* browser trigger the cookie as safe, and only be send by secure connection.
CSRF_COOKIE_SECURE = True if DEBUG == False else False
CSRF_USE_SESSIONS = True if DEBUG == False else False
#* CSRF cookies can only be access by https request.
CSRF_COOKIE_HTTPONLY = True