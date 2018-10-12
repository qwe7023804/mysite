from django.conf.urls import url
from django.urls import path
from user_app import views_if

urlpatterns = [
    path('add_project/', views_if.add_project, name='add_project'),
    path('get_project_list/', views_if.get_project_list, name='get_project_list'),
    path('edit_project/', views_if.edit_project, name='edit_project'),
    path('delete_project/', views_if.delete_project, name='delete_project'),
]
