from django.contrib import admin
from django.urls import path
from . import  views
urlpatterns = [
    path('', views.empty, name='empty'),
        path('viewAll',views.viewAll , name="viewAllTasks"),
        path("addTask",views.addTask,name="addTask"),
        path('update/<int:id>', views.update, name="update"),
        path('delete/<int:id>',views.delete,name="delete"),

]
