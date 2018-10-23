from django.conf.urls import url
from django.urls import path
from project_app import views_project, views_module

urlpatterns = [
    path('home/', views_project.home, name='home'),
    path('create_project/', views_project.create_project, name='create_project'),
    path('add_project/', views_project.add_project, name='add_project'),
    path('get_project_list/', views_project.get_project_list, name='get_project_list'),
    path('edit_project/', views_project.edit_project, name='edit_project'),
    path('delete_project/', views_project.delete_project, name='delete_project'),

    path('module/', views_module.module, name='module'),
    path('create_module/', views_module.create_module, name='create_module'),
    path('add_module/', views_module.add_module, name='add_module'),
]
