# backend/serializers.py
from rest_framework import serializers
from .models import Month, Customer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password')
    extra_kwargs = {'password':{'write_only':True,'required':True}}

  def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      print(user)
      Token.objects.create(user=user)
      return user

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'
        extra_kwargs = {'navn': {'required':True}}

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'



