# backend/views.py
from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Month, Customer
from .serializers import MonthSerializer, CustomerSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_extensions.mixins import NestedViewSetMixin

class UserViewSet(NestedViewSetMixin, ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (AllowAny, )


class MonthViewSet(NestedViewSetMixin, ModelViewSet):
    queryset=Month.objects.all()
    serializer_class = MonthSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )

class CustomerViewset(NestedViewSetMixin, ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, )
