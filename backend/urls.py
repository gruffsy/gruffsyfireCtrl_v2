from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from backend import views

urlpatterns = [
    path('months/', views.MonthList.as_view()),
    path('months/<int:pk>/', views.MonthDetail.as_view()),
]