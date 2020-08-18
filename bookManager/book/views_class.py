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
    