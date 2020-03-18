import graphene
from graphene_django.types import DjangoObjectType
from .models import Month

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


class Query(graphene.ObjectType):
    month = graphene.Field(MonthType, id=graphene.Int())
    months = graphene.List(MonthType)

    def resolve_month(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Month.objects.get(pk=id)

        return None

    def resolve_months(self, info):
        return Month.objects.all()

class Mutations(graphene.ObjectType):
    create_month = CreateMonth.Field()