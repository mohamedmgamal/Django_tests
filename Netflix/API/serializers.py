from rest_framework import serializers
from Netflix.models import ApiTest
from django.contrib.auth.models import User
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApiTest
        fields="__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"