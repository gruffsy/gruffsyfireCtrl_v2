import graphene
import fireCtrl_app.schema

class Query(fireCtrl_app.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(fireCtrl_app.schema.Mutations, graphene.ObjectType):
  	pass

schema = graphene.Schema(query=Query,mutation=Mutation)