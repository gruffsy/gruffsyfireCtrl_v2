# backend/views.py
from .serializers import *
from rest_framework import generics


class MonthList(generics.ListCreateAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer

class MonthDetail(generics.RetrieveUpdateAPIView):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer