import graphene
import ingredients.schemas

class Query(ingredients.schemas.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)