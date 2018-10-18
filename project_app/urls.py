from django.conf.urls import url
from django.urls import path
from project_app import views

urlpatterns = [
    path('home/', views.home),
    path('create_project/', views.create_project, name='create_project'),
    path('add_project/', views.add_project, name='add_project'),
    path('get_project_list/', views.get_project_list, name='get_project_list'),
    path('edit_project/', views.edit_project, name='edit_project'),
    path('delete_project/', views.delete_project, name='delete_project'),
]
