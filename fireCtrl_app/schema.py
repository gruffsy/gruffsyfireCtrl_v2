import graphene
from graphene_django.types import DjangoObjectType
from .models import Month, Customer, Slokketype, Extinguishant, Objekt

# Modell Month
class MonthType(DjangoObjectType):
    class Meta:
        model = Month

class CreateMonth(graphene.Mutation):
    ok = graphene.Boolean()
    month = graphene.Field(lambda: MonthType)

    class Arguments:
        navn = graphene.String()
        
    def mutate(self, info, navn):
        month = Month(navn=navn)
        month.save()
        ok = True
        return CreateMonth(month=month,ok=ok)

# Model Customer
class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer

# Model Slokketype
class SlokketypeType(DjangoObjectType):
    class Meta:
        model = Slokketype
    
# Model Extinguishant
class ExtinguishantType(DjangoObjectType):
    class Meta:
        model = Extinguishant

#Model Objekt
class ObjektType(DjangoObjectType):
    class Meta:
        model = Objekt

class Query(graphene.ObjectType):
    month = graphene.Field(MonthType, id=graphene.Int())
    months = graphene.List(MonthType)

    customer = graphene.Field(CustomerType, id=graphene.Int())
    customers = graphene.List(CustomerType)

    slokketype = graphene.Field(SlokketypeType, id=graphene.Int())
    slokketypes = graphene.List(SlokketypeType)

    extinguishant = graphene.Field(ExtinguishantType, id=graphene.Int())
    extinguishants = graphene.List(ExtinguishantType)

    objekt = graphene.Field(ObjektType, id=graphene.Int())
    objekts = graphene.List(ObjektType)

    # sinle queries

    def resolve_month(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Month.objects.get(pk=id)

        return None

    def resolve_customer(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Customer.objects.get(pk=id)

        return None

    def resolve_slokketype(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Slokketype.objects.get(pk=id)

        return None

    def resolve_extinguishant(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Extinguishant.objects.get(pk=id)

        return None

    def resolve_objekt(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Objekt.objects.get(pk=id)

        return None

    # mange queries
    def resolve_months(self, info):
        return Month.objects.all()
    
    def resolve_customers(self, info):
        return Customer.objects.all()

    def resolve_slokketypes(self, info):
        return Slokketype.objects.all()

    def resolve_extinguishants(self, info):
        return Extinguishant.objects.all()
    
    def resolve_objekts(self, info):
        return Objekt.objects.all()




class Mutations(graphene.ObjectType):
    create_month = CreateMonth.Field()