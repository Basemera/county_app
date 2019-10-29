import graphene
from country_list.schema.query.country import Query as CountryQuery
from country_list.schema.query.city import Query as CityQuery
from country_list.schema.query.subcountry import Query as SubCountryQuery
from country_list.schema.mutations.country import Mutation as CreateCountryMutation
from auth.schema.mutations.register import Mutation as RegisterUser


class Query(CountryQuery, CityQuery, SubCountryQuery, graphene.ObjectType):
    pass

class Mutation(CreateCountryMutation, RegisterUser, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)