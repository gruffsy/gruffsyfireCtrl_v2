# backend/serializers.py
from rest_framework import serializers
from .models import Month, Customer, Object, Slokketype, Extinguishant, Avvik, ObjTr
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        print(user)
        Token.objects.create(user=user)
        return user


class MonthSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Month
        fields = '__all__'
        extra_kwargs = {'navn': {'required': True}}


class CustomerSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'


class SlokketypeSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Slokketype
        fields = '__all__'


class ExtinguishantSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Extinguishant
        fields = '__all__'


class EtgSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)
    
       
    class Meta:  
        model = Object  
        fields = ['etg']

class LokasjonSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)
    
       
    class Meta:  
        model = Object  
        fields = ['etg', 'lokasjon']

class PlasseringSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)
    
       
    class Meta:  
        model = Object  
        fields = ['etg', 'lokasjon', 'plassering']


class ObjectSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)
    
       
    class Meta:  
        model = Object  
        fields = '__all__'

class AvvikSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Avvik
        fields = '__all__'

class ObjTrSerializer(serializers.ModelSerializer):
   # id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ObjTr
        fields = '__all__'


