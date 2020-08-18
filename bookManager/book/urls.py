from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    # django=2.2.5版本，不能写成：path('^index/', views.index)
    path('index/', views.index),
    path('hobby/', views.hobby),
    path('<category_id>/<product_id>/', views.detail),
    path('search/', views.search),
    path('form_data/', views.form_data),
    path('json_data/', views.json_data),
    path('header_data/', views.header_data),
    path('redirect_url/', views.redirect_url),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path('del_cookie/', views.del_cookie),
    path('set_session/', views.set_session),

    # 类视图
    path('regist/', views.RegistView.as_view()),
    path('login/', views.LoginView.as_view()),

]
