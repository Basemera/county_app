import graphene
from graphene_django import DjangoObjectType

from country_list.models import *

class CreateCity(graphene.Mutation):
    id = graphene.Int()
    city_name = graphene.String()
    subcountry_id = graphene.Int()

    class Arguments:
        city_name = graphene.String()
        subcountry_id = graphene.Int()
    

    def mutate(self, info, city_name, subcountry_id):
        subcountry = SubCountry.objects.get(pk=subcountry_id)
        city = City(city_name=city_name, subcountry=subcountry)
        city.save()

        return CreateCity(
            id=city.id,
            city_name = city.city_name,
            subcountry_id = city.subcountry
        )

class Mutation(graphene.ObjectType):
    create_city = CreateCity.Field()
