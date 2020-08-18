from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from book.views_class import *
from django.conf import global_settings

# Create your views here.
def index(request):
    # settings.DEFAULT_CHARSET = 'utf-8'
    # settings.DEFAULT_CONTENT_TYPE = 'text/html'
    return HttpResponse("这是一个index首页", content_type="text/html; charset=utf-8", status="200", charset="utf-8")
    # 设置响应application/json,但是响应的数据不是json串,页面也不会报错,也会正常显示.因为request请求头中的Accept:*/*,表示可以接受任意数据类型.
    # return HttpResponse("这是一个index首页", content_type="application/json", status="200", charset="utf-8")

def hobby(request):
    return render(request, template_name="book/html/index.html", context={"hobby": "阅读"})


# 关键字传参.第1个参数必须是request
def detail(request, product_id, category_id):
    print(request.path)
    print(request.encoding)  # None
    query_dict = request.GET
    print(query_dict)
    return HttpResponse("category_id=%s, product_id=%s" % (category_id, product_id))

# 查询字符串
def search(request):
    # 不包含查询字符串
    print(request.path)
    # 提交的数据的编码方式.如果返回None,表示使用浏览器的默认设置,一般为utf-8
    print(request.encoding)  # None
    key = request.GET.get("keyword")
    keys = request.GET.getlist("keyword")
    # QueryDict中的key对应的value是个list.get()方法永远获取的是list中的最后一个元素.getlist()获取的是整个列表.
    print(request.GET, key, keys)
    key1 = request.GET.get("name", "lucy")
    keys1 = request.GET.getlist("name", "lucy")
    # get():当获取的key不存在时,返回None,如果指定了默认值,则返回默认值.
    # getlist():当获取的key不存在,返回一个空列表,如果指定了默认值,则返回默认值.
    print(key1, keys1)
    # JsonRequest做了2件事,1是将字典转为json串,2是设置响应头Content_Type="application/json".(默认值是text/html)
    return JsonResponse({"keyword": keys})

# 表单类型的数据
def form_data(request):
    u = request.user
    p = request.path
    # AnonymousUser     # <class 'django.utils.functional.SimpleLazyObject'>
    print(u, type(u))
    # /form_data/   # <class 'str'>
    print(p, type(p))
    name = request.POST.get("name")
    pwd = request.POST.get("password")
    return JsonResponse({"name": name, "password": pwd})

# json格式的数据
def json_data(request):
    bytes_data = request.body
    str_data = bytes_data.decode("utf-8")
    print(type(str_data), "\n", str_data)
    return JsonResponse(str_data, safe=False)   # "{\n\t\"name\": \"lucy\",\n\t\"age\": 34,\n\t\"gender\": 1\n}"

# 请求头数据
def header_data(request):
    # 通过META属性获取请求头部信息
    dict_data = request.META
    print(dict_data)
    # 必须是HTTP规定好的请求头,自己定义的不可以用,不认识
    return HttpResponse(dict_data["CONTENT_TYPE"])  # 需要大写


# 重定向
def redirect_url(request):
    # 如果想跳转到第三方网站,需要写上http://,如果不写,就会跳转到 /redirect_url/baidu.com/,正好匹配了path('<category_id>/<product_id>/', views.detail)
    return redirect(to="http://baidu.com")
    # return redirect("/index/")