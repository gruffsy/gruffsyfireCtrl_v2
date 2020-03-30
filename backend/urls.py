from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MonthViewSet, CustomerViewset, UserViewSet


router = routers.DefaultRouter()
router.register('months', MonthViewSet)
router.register('customers', CustomerViewset)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]