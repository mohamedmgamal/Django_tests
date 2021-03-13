from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('', views.empty, name='empty'),
    path('home', views.viewAll, name='home'),
]
