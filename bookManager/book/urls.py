from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    # django=2.2.5版本，不能写成：path('^index/', views.index)
    path('index/', views.index),
    path('hobby/', views.hobby),
]
