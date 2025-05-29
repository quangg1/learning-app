from django.http import HttpRequest
#* import class MiddlewareMixin
from django.utils.deprecation import MiddlewareMixin
from dev_core.security.cache.cache_dev import CacheDecoratorFactory

class HiddenInfoMiddleware:
    """
    Middleware to force users to log in before accessing any page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # print(CacheDecoratorFactory.cache_manager.get_cache_page("length"))
        response = self.get_response(request)
        #* Hidden Info Middleware
        response.__setitem__('X-Content-Type-Options', 'nosniff')
        response.__setitem__('X-Frame-Options', 'DENY')
        response.__setitem__('X-XSS-Protection', '1; mode=block')
        response.__setitem__('Feature-Policy', "geolocation 'none'")
        response.__setitem__('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        response.__setitem__('Cache-Control', 'no-cache, no-store, must-revalidate')
        response.__setitem__('Pragma', 'no-cache')
        # response.__setitem__('Content-Security-Policy', "script-src 'self' https://apis.google.com")
        response.__setitem__('Server', '')
        response.headers['Server'] = "None of your beeswax!"
        return response
    
    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
        return None
    