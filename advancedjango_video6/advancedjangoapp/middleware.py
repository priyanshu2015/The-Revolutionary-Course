from django.utils.deprecation import MiddlewareMixin
import threading
class CustomMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self._async_check()

    def process_request(self, request):
        print(threading.get_native_id())
        print("I am in this middleware, request part")
        #print(self._is_coroutine)

    def process_response(self, request, response):
        print(threading.get_native_id())
        print("I am in this middleware")
        #print(self._is_coroutine)
        return response