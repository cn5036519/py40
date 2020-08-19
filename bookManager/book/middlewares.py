from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


# 自定义中间件
"""
TestMiddleware与Test2Middleware这两个中间件的执行顺序:
    当请求过来时,会按照中间件的注册顺序,依次执行process_request()方法,前提是这个方法必须return None.
    当视图函数response响应后,按照中间件的注册顺序,倒叙依次执行process_response()方法,但这个方法必须return response,否则报错.
"""
class TestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("test1中间件 ---process_request")

    def process_response(self, request, response):
        print("test1中间件 ---process_response")
        return response


class Test2Middleware(MiddlewareMixin):
    def process_request(self, request):
        print("test2中间件 ---process_request")

    def process_response(self, request, response):
        print("test2中间件 ---process_response")
        return response


"""
Test3Middleware与Test4Middleware这两个中间件的执行顺序:
    这两个类都没有重写process_response()方法.
    当执行到中间件3的process_request()方法时,它返回了一个response对象,所以,它不再往后执行,(中间件4和视图函数都不会执行了)
    紧接着倒叙执行中间件2\中间件1的process_response()方法.
"""
# 异常流程
class Test3Middleware(MiddlewareMixin):
    def process_request(self, request):
        print("test3中间件 ---process_request")
        return HttpResponse("ok")


class Test4Middleware(MiddlewareMixin):
    def process_request(self, request):
        print("test4中间件 ---process_request")


"""
Test5Middleware与Test6Middleware中间件的执行流程:
    按照中间件的注册顺序,依次执行process_view()方法,前提是这个方法必须return None.
    然后再执行视图函数.
    最后倒叙依次执行process_response()方法.
"""
class Test5Middleware(MiddlewareMixin):
    def process_request(self, request):
        print("test5中间件 ---process_request")

    def process_response(self, request, response):
        print("test5中间件 ---process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("test5中间件 ---process_view")


class Test6Middleware(MiddlewareMixin):
    def process_request(self, request):
        print("test6中间件 ---process_request")

    def process_response(self, request, response):
        print("test6中间件 ---process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("test6中间件 ---process_view")


"""
Test7Middleware中间件的执行流程:
    当执行到中间件7的process_view()方法,发现返回了一个response对象,则就不再完后执行,(不执行后面的中间件\视图函数)
    紧接着执行中间件7以及后面中间件的process_response()方法.
"""
# 异常流程
class Test7Middleware(MiddlewareMixin):
    def process_request(self, request):
        print("test7中间件 ---process_request")

    def process_response(self, request, response):
        print("test7中间件 ---process_response")
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("test7中间件 ---process_view")
        return HttpResponse("OKOK")