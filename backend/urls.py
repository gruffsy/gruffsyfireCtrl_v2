from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import include
from .views import *
from rest_framework_extensions.routers import NestedRouterMixin


router = DefaultRouter()
router.register('months', MonthViewSet)
router.register('customers', CustomerViewset)
router.register('users', UserViewSet)
router.register('objects', ObjectViewset)
router.register('slokketypes', SlokketypeViewset)
router.register('extinguishants', ExtinguishantViewset)
router.register('avviks', AvvikViewset)
router.register('objtrs', ObjTrViewset)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

months_router = router.register('months', MonthViewSet)
months_router.register(
    'customers', CustomerViewset,
    basename='month-customers',
    parents_query_lookups=['month']
    )#.register('objects', ObjectViewset, basename='month-customers-object', parents_query_lookups= ['customer__month', 'customer'])


customers_router = router.register('customers', CustomerViewset)
users_router = router.register('users', UserViewSet)
objects_router = router.register('objects', ObjectViewset)
slokketypes_router = router.register('slokketypes', SlokketypeViewset)
extinguishants_router = router.register('extinguishants', ExtinguishantViewset)
avviks_router = router.register('avviks', AvvikViewset)
objtrs_router = router.register('objtrs', ObjTrViewset)

urlpatterns = [
    path('', include(router.urls)),
]
