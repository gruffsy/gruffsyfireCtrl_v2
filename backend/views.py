# backend/views.py
import django_filters
from django.shortcuts import render
from rest_framework import status, filters
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework_extensions.mixins import NestedViewSetMixin
from url_filter.integrations.drf import DjangoFilterBackend
from .filters import KontrollFilter
from django.db.models import Prefetch

class UserViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    permission_classes = (AllowAny, )


class MonthViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Month.objects.all()
    serializer_class = MonthSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )


class CustomerViewset(NestedViewSetMixin, ModelViewSet):
    #queryset = Customer.objects.all()
    queryset = Customer.objects.prefetch_related(Prefetch(
        'objekter',
        queryset=Object.objects.all()))
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    authentication_classes = (
        TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )
    filters_custom = django_filters.DateTimeFilter(name=("modified", "created", "objekter__sistekontroll"), lookup_expr=('gte', 'lte', 'gt', 'lt'))


    def get_queryset(self):
        queryset = super(CustomerViewset, self).get_queryset()

        order_by = self.request.query_params.get('order_by', '')
        if order_by:
            order_by_name = order_by.split(' ')[1]
            order_by_sign = order_by.split(' ')[0]
            order_by_sign = '' if order_by_sign == 'asc' else '-'
            queryset = queryset.order_by(order_by_sign + order_by_name)

        return queryset


class SlokketypeViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Slokketype.objects.all()
    serializer_class = SlokketypeSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )


class ExtinguishantViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Extinguishant.objects.order_by('fabrikat', 'type', 'lengde', 'slukkemiddel')
    serializer_class = ExtinguishantSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    


class EtgViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Object.objects.group_by('etg').order_by('etg').distinct()
    serializer_class = EtgSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    filters_custom = django_filters.DateTimeFilter(name=("modified", "created", "nestekontroll"), lookup_expr=('gte', 'lte', 'gt', 'lt'))

class LokasjonViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Object.objects.group_by('lokasjon', 'etg').order_by('etg', 'lokasjon').distinct()
    serializer_class = LokasjonSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    filters_custom = django_filters.DateTimeFilter(name=("modified", "created", "nestekontroll"), lookup_expr=('gte', 'lte', 'gt', 'lt'))

class PlasseringViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Object.objects.group_by('plassering', 'lokasjon', 'etg').order_by('etg', 'lokasjon', 'plassering').distinct()
    serializer_class = PlasseringSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    filters_custom = django_filters.DateTimeFilter(name=("modified", "created", "nestekontroll"), lookup_expr=('gte', 'lte', 'gt', 'lt'))
    




class ObjectViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    filters_custom = django_filters.DateTimeFilter(name=("modified", "created", "nestekontroll"), lookup_expr=('gte', 'lte', 'gt', 'lt'))
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = super(ObjectViewset, self).get_queryset()

        order_by = self.request.query_params.get('order_by', '')
        if order_by:
            order_by_name = order_by.split(' ')[1]
            order_by_sign = order_by.split(' ')[0]
            order_by_sign = '' if order_by_sign == 'asc' else '-'
            queryset = queryset.order_by(order_by_sign + order_by_name)

        return queryset


class AvvikViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Avvik.objects.all()
    serializer_class = AvvikSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )


class ObjTrViewset(NestedViewSetMixin, ModelViewSet):
    queryset = ObjTr.objects.all()
    serializer_class = ObjectSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = '__all__'
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

class PrevCustomerViewset(NestedViewSetMixin, ModelViewSet):
    queryset = Object.objects.order_by('-modified')
    queryset = queryset.all()[:1]
    #queryset = queryset.group_by('customer')
    serializer_class = ObjectSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication, BasicAuthentication)

    