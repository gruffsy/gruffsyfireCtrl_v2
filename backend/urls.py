from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import MonthViewSet, CustomerViewset, UserViewSet
from rest_framework_extensions.routers import NestedRouterMixin


router = DefaultRouter()
router.register('months', MonthViewSet)
router.register('customers', CustomerViewset)
router.register('users', UserViewSet)


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

months_router = router.register('months', MonthViewSet)
months_router.register(
    'customers',
    CustomerViewset,
    basename='month-customers',
    parents_query_lookups=['month']
)
customers_router = router.register('customers', CustomerViewset)


urlpatterns = [
    path('', include(router.urls)),
]
