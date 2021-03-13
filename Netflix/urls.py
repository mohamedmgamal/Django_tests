from django.urls import path
from . import  views
urlpatterns = [
    path('', views.viewAll, name='viewAll'),
    path('addMovie',views.addMovie,name='addMovie'),
    path('editMovie/<int:id>',views.edit,name='editMovie'),
    path('deleteMovie/<int:id>',views.delete,name='deleteMovie')
]
