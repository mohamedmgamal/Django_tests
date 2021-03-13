from django.urls import path
from . import  views
urlpatterns = [
    path('', views.viewAll, name='viewAll'),
    path('addMovie',views.addMovie,name='addMovie')
]
