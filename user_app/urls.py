from django.conf.urls import url
from django.urls import path
from user_app import views_if

urlpatterns = [
    path('add_project/', views_if.add_project, name='add_project'),
    path('get_project_list', views_if.get_project_list, name='get_project_list'),
]
