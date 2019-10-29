import graphene
from country_list.schema.query.country import Query as CountryQuery
from country_list.schema.query.city import Query as CityQuery
from country_list.schema.query.subcountry import Query as SubCountryQuery
from country_list.schema.mutations.country import Mutation as CreateCountryMutation
from auth.schema.mutations.register import Mutation as RegisterUser
from country_list.schema.mutations.city import Mutation as CreateCityMutation



class Query(CountryQuery, CityQuery, SubCountryQuery, graphene.ObjectType):
    pass

class Mutation(CreateCountryMutation, RegisterUser, graphene.ObjectType):
    class Mutation(CreateCountryMutation, CreateCityMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
