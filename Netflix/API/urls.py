from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
path('',views.index),
path('create',views.create),
path('login/', obtain_auth_token, name='api_token_auth'),
path('update/<int:id>/',views.Update),
path('signUp/',views.signUp)
]
