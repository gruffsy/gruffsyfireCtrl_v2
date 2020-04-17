from .models import Object
import django_filters

class KontrollFilter(django_filters.FilterSet):
    kontroll = django_filters.DateTimeFilter( label='Kontrollert')
    sistekontroll = django_filters.DateTimeFilter(name='sistekontroll', lookup_expr='exact')

    class Meta:
       model = Object
       fields = ['sistekontroll']