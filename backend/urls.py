from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import MonthViewSet, CustomerViewset, UserViewSet, ObjectViewset
from rest_framework_extensions.routers import NestedRouterMixin


router = DefaultRouter()
router.register('months', MonthViewSet)
router.register('customers', CustomerViewset)
router.register('users', UserViewSet)
router.register('objects', ObjectViewset)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

months_router = router.register('months', MonthViewSet)
months_router.register(
    'customers', CustomerViewset,
    basename='month-customers',
    parents_query_lookups=['month']
    ).register(
        'objects', ObjectViewset,
        basename='month-customers-object',
        parents_query_lookups= ['customer__month', 'customer']
        )



customers_router = router.register('customers', CustomerViewset)
users_router = router.register('users', UserViewSet)
objects_router = router.register('objects', ObjectViewset)
urlpatterns = [
    path('', include(router.urls)),
]
