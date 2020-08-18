from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View


class RegistView(View):
    def get(self, request):
        return HttpResponse("regist功能-get请求")

    def post(self, request):
        return HttpResponse("regist功能-post请求")

    def put(self, request):
        return HttpResponse("regist功能-put请求")

    def delete(self, request):
        return HttpResponse("regist功能-delete请求")

    def patch(self, request):
        return HttpResponse("regist功能-patch请求")

    def head(self, request):
        return HttpResponse("regist功能-head请求")

    def options(self, request):
        return HttpResponse("regist功能-options请求")

    def trace(self, request):
        return HttpResponse("regist功能-trace请求")


# class LoginView(View, LoginRequiredMixin):
class LoginView(LoginRequiredMixin, View):
    """
    LoginRequiredMixin类的dispatch()方法增加了登录验证功能.
    LoginRequiredMixin类中实现了dispatch()方法,就不再调用View类中的dispatch()方法.
    
    """
    def get(self, request):
        return HttpResponse("login功能-get请求")

    def post(self, request):
        return HttpResponse("login功能-post请求")
