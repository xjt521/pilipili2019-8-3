from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from log_reg import  views

urlpatterns = [

    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]
