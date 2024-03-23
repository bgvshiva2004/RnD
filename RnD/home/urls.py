from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.homepage,name='homepage'),
    # path('monthly/',views.monthly,name='monthly'),
    path('login/',views.login,name='login'),
    path('project_list/',views.project_list,name='project_list'),
    path('project_listwise/',views.project_listwise,name='project_listwise'),
    path('fill/<int:project_id>/',views.fill,name='fill'),
    path('mastersheet/<int:project_id>/',views.mastersheet,name='mastersheet'),
    # path('save_data_to_file/', views.save_data_to_file, name='save_data_to_file'),
     path('save_table_data1/<int:project_id>/', views.save_table_data1, name='save_table_data1'),
    path('save_table_data/<int:project_id>/',views.save_table_data,name='save_table_data'),
    path('save_tables_to_file/<int:project_id>/', views.save_tables_to_file, name='save_tables_to_file'),
    path('logout/',views.logout,name='logout'),
    path('project_search/', views.project_search, name='project_search'),
    path('complete_task/<int:project_id>/', views.complete_task, name='complete_task'),
    path('soe/<int:project_id>/',views.soe,name='soe'),
    path('ucr/<int:project_id>/',views.ucr,name='ucr'),
    path('SOE_navigation/<int:project_id>/',views.SOE_navigation,name='SOE_navigation'),
    path('UCR_navigation/<int:project_id>/',views.UCR_navigation,name='UCR_navigation'),
    path('UCNR_navigation/<int:project_id>/',views.UCNR_navigation,name='UCNR_navigation'),
    path('soe/<int:project_id>/<str:period>/', views.soe, name='soe'),
    path('ucr/<int:project_id>/<str:period>/',views.ucr,name='ucr'),
    path('ucnr/<int:project_id>/',views.ucr,name='ucnr'),
    path('ucnr/<int:project_id>/<str:period>/',views.ucnr,name='ucnr'),
    path('save-as-pdf/', views.save_as_pdf, name='save_as_pdf'),
    path('save-as-excel/', views.save_as_excel, name='save_as_excel'),
    path('download-pdf/', views.download_pdf, name='download_pdf'),
    path('download-excel/', views.download_excel, name='download_excel'),
    path('submit_project_data/<int:project_id>/', views.submit_project_data, name='submit_project_data'),
    path('delete_project/<int:project_id>/',views.delete_project,name='delete_project'),
    path('save_info/<int:project_id>/', views.save_info, name='save_info'),

]