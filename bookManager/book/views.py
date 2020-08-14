from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("这是一个index首页")

def hobby(request):
    return render(request, template_name="book/html/index.html", context={"hobby": "阅读"})
