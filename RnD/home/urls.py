from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.homepage,name='homepage'),
    path('monthly/',views.monthly,name='monthly'),
    path('login/',views.login,name='login'),
    path('project_list/',views.project_list,name='project_list'),
    path('project_listwise/',views.project_listwise,name='project_listwise'),
    path('fill/<int:project_id>/',views.fill,name='fill'),
    path('mastersheet/<int:project_id>/',views.mastersheet,name='mastersheet'),
    path('save_data_to_file/', views.save_data_to_file, name='save_data_to_file'),
     path('save_table_data1/<int:project_id>/', views.save_table_data1, name='save_table_data1'),
    path('save_table_data/<int:project_id>/',views.save_table_data,name='save_table_data'),
    path('save_tables_to_file/<int:project_id>/', views.save_tables_to_file, name='save_tables_to_file'),
    path('logout/',views.logout,name='logout'),
    path('project_search/', views.project_search, name='project_search'),
    path('complete_task/<int:project_id>/', views.complete_task, name='complete_task'),
    path('soe/<int:project_id>/',views.soe,name='soe'),
    path('ucr/',views.ucr,name='ucr')
]