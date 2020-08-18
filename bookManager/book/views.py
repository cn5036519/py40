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


def set_cookie(request):
    """
    服务器端设置cookie,然后响应给客户端,浏览器再保存到本地电脑.
    每当浏览器访问页面时,都会携带该网站的所有cookie.
    """
    # 响应头增加了Set-Cookie: age=34; Path=/
    response = HttpResponse("服务器端设置cookie")
    response.set_cookie('name', 'alex')
    # 设置cookie的有效时间为5秒
    response.set_cookie('age', 34, max_age=5)
    # 不设置cookie的有效时间,则默认为None,即浏览器一次回话结束则失效.
    response.set_cookie('gender', 1)
    print(response.cookies)
    """
    测试结果:
        Set-Cookie: age=34; Path=/
        Set-Cookie: gender=1; Path=/
        Set-Cookie: name=alex; Path=/
    """
    print(type(response.cookies))   # <class 'http.cookies.SimpleCookie'>
    return response


def get_cookie(request):
    # 请求头增加了 Cookie: name=alex; age=34; gender=1
    print(request.COOKIES)  # {'name': 'alex', 'age': '34', 'gender': '1'}
    print(type(request.COOKIES))    # <class 'dict'>
    return JsonResponse(request.COOKIES)


def del_cookie(request):
    response = JsonResponse(request.COOKIES)
    # 底层实现,就是设置gender的过期时间为0
    response.delete_cookie("gender")
    return response


def set_session(request):
    """
    设置session,session的数据会默认存储在数据库中,同时,在服务器端设置了一个key叫sessionid的cookie信息,会把它响应给客户端. 如下:
        Set-Cookie: sessionid=cyrbmci1qc9nwiwewj6pm28y5yodo2ik; expires=Tue, 01 Sep 2020 12:50:33 GMT; HttpOnly; Max-Age=1209600; Path=/; SameSite=Lax
    客户端下次访问网页时,会携带此cookie,服务器会根据此进行判断,如果正确,那么服务器和客户端就保持了状态连接.
    """
    print(request.session)  # <django.contrib.sessions.backends.db.SessionStore object at 0x7f819a432a58>
    print(type(request.session))    # <class 'django.contrib.sessions.backends.db.SessionStore'>
    # 设置session
    request.session["user_id"] = "140501198710092927"
    request.session["user_name"] = "jackc"
    # 设置session的有效期.设置为None,则使用系统的默认过期时间,即两周. 设置为0,表示关闭浏览器即过期.
    # 有效期过后,数据库中的数据并没有删除,需要手动删除.客户端存储的key为sessionid的cookie会自动删除.
    request.session.set_expiry(30)
    return HttpResponse("设置session")


def get_session(request):
    id = request.session.get("user_id")
    name = request.session.get("user_name")
    return HttpResponse("获取到的session: user_id=%s, user_name=%s" % (id, name))


def clear_session(request):
    # 清除session:删除在数据库存储的值,key仍保留.同时,服务器重新设置了cookie信息,把它响应给了客户端.
    request.session.clear()
    # 清除了session,key存在,但值已经被删除了,因此打印None
    print(request.session.get("user_id", None))
    return HttpResponse("清除session")


def flush_session(request):
    """刷新cookie:删除了在数据库存储的整条数据,同时,服务器重新设置了cookie并响应给客户端.如下:
            Set-Cookie: sessionid=""; expires=Thu, 01 Jan 1970 00:00:00 GMT; Max-Age=0; Path=/
    """
    request.session.flush()
    try:
        print(request.session.get("user_id", None))
    except Exception as e:
        print("出错了")
    return HttpResponse("刷新session")


def delete_session(request):
    """
    删除cookie:删除了在数据库存储的整条数据,但是,服务器没有重新设置cookie并响应给客户端.所以,浏览器仍存储着删除了的key为sessionid的cookie信息.

    """
    request.session.delete()
    return HttpResponse("删除session")