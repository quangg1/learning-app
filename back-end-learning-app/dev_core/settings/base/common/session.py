#* #** Security settings for the session middleware
from dev_core.settings.settings import *


#* The domain to use for session cookies. 
SESSION_COOKIE_SAMESITE = 'Strict' if DEBUG == False else 'Lax'
#* browser trigger the session cookie as safe, and only be send by secure connection.
SESSION_COOKIE_SECURE = True if DEBUG == False else False
#* The session cookie will be sent on every request.
SESSION_SAVE_EVERY_REQUEST = True if DEBUG == False else False
#* session cookies can only be access by https request.
SESSION_COOKIE_HTTPONLY = True