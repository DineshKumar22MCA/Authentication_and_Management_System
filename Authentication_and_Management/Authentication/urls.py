from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *




urlpatterns = [
    path('',index,name="index"),
    path('signup',signup,name="signup"),
    path('signin',signin,name="signin"),
    path('reset_password',reset_password,name="reset_password"),
    path('home',home,name="home"),
    path('add', insert,name="insert"),
    path('edit/<int:id>',edit,name="edit"),
    path('delete/<int:id>',delete,name="delete"),
    path('signout',signout, name='signout'),
    path('admin/', admin.site.urls),
]