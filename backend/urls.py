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
router.register('etgs', EtgViewset)
router.register('lokasjons', LokasjonViewset)
router.register('plasserings', PlasseringViewset)
router.register('cust_objects', CustomerViewset)
router.register('prev_customers', PrevCustomerViewset)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
# api/months/{monthId}/customers/{customerId}/etgs/
months_cust_router = router.register('months', MonthViewSet)
months_cust_router.register('customers', CustomerViewset, basename='month-customers', parents_query_lookups=['month']
).register('etgs', EtgViewset, basename="month-customer-etgs", parents_query_lookups=['customer__month', 'customer']
)

# api/customers/{customerId}/etgs/
cust_etg_router = router.register('customers', CustomerViewset)
cust_etg_router.register('etgs', EtgViewset, basename='customer-etgs', parents_query_lookups= ['customer'])

# api/customers/{customerId}/lokasjons/
cust_lok_router = router.register('customers', CustomerViewset)
cust_lok_router.register('lokasjons', LokasjonViewset, basename='customer-lokasjons', parents_query_lookups= ['customer'])

# api/customers/{customerId}/plasserings/
cust_plasserings_router = router.register('customers', CustomerViewset)
cust_plasserings_router.register('plasserings', PlasseringViewset, basename='customer-plasserings', parents_query_lookups= ['customer'])

# api/customers/{customerId}/objects/
cust_objects_router = router.register('customers', CustomerViewset)    
cust_objects_router.register('objects', ObjectViewset, basename="customer-objects", parents_query_lookups= ['customer'])

prev_customer_router = router.register('prev_customers', PrevCustomerViewset)
months_router = router.register('months', MonthViewSet)
customers_router = router.register('customers', CustomerViewset)
users_router = router.register('users', UserViewSet)
objects_router = router.register('objects', ObjectViewset)
slokketypes_router = router.register('slokketypes', SlokketypeViewset)
extinguishants_router = router.register('extinguishants', ExtinguishantViewset)
avviks_router = router.register('avviks', AvvikViewset)
objtrs_router = router.register('objtrs', ObjTrViewset)
etgs_router = router.register('etgs', EtgViewset)

urlpatterns = [
    path('', include(router.urls)),
]
