from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('delete', views.delete, name='delete'),
    path('tasks', views.index, name='index'),
    path('<str:name>', views.welcome, name='welcome')

]
