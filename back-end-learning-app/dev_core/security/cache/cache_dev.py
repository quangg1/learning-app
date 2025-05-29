from abc import ABC, abstractmethod
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from typing import *

class CacheStrategy(ABC):
    @abstractmethod
    def cache_decorator(self, timeout):
        pass

class CookieCacheStrategy(CacheStrategy):
    def cache_decorator(self, timeout):
        return method_decorator(cache_page(timeout))(method_decorator(vary_on_cookie))

class AuthCacheStrategy(CacheStrategy):
    def cache_decorator(self, timeout):
        return method_decorator(cache_page(timeout))(method_decorator(vary_on_headers("Authorization")))

class SimpleCacheStrategy(CacheStrategy):
    def cache_decorator(self, timeout):
        return method_decorator(cache_page(timeout))
    
class CacheManager:
    def __init__(self):
        self.cache = {}

    def get_cache_page(self, page_key):
        return self.cache.get(page_key)

    def set_cache_page(self, page_key, cached_page):
        self.cache[page_key] = cached_page

    def clear_cache_page(self, page_key):
        if page_key in self.cache:
            del self.cache[page_key]
    
class CacheDecoratorFactory:
    cookie_cache_strategy = CookieCacheStrategy()
    auth_cache_strategy = AuthCacheStrategy()
    simple_cache_strategy = SimpleCacheStrategy()
    #* Inject the desired cache strategy
    cache_manager = CacheManager()  
    count = 0
    @staticmethod
    def create_cache_decorator(strategy: Literal["cookie", "auth", "simple"] = "simple", timeout=60*15): #* 15 minutes
        CacheDecoratorFactory.count += 1
        CacheDecoratorFactory.cache_manager.set_cache_page("length", CacheDecoratorFactory.count)        
        if strategy == "cookie":
            return CacheDecoratorFactory.cookie_cache_strategy.cache_decorator(timeout)
        elif strategy == "auth":
            return CacheDecoratorFactory.auth_cache_strategy.cache_decorator(timeout)
        else:
            return CacheDecoratorFactory.simple_cache_strategy.cache_decorator(timeout)
        
       
# Example usage


#* Select the desired cache strategy
cache_decorator_factory = CacheDecoratorFactory()


