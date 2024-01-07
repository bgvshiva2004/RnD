from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.homepage,name='homepage'),
    path('monthly/',views.monthly,name='monthly'),
    path('login/',views.login,name='login'),
    path('project_list/',views.project_list,name='project_list'),
]