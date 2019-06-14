import graphene
from graphene_django import DjangoObjectType

from country_list.models import Country

class CreateCountry(graphene.Mutation):
    id = graphene.Int()
    country_name = graphene.String()
    geonameid = graphene.Int()

    class Arguments:
        country_name = graphene.String()
        geonameid = graphene.Int()
    

    def mutate(self, info, country_name, geonameid):
        country = Country(country_name=country_name, geonameid=geonameid)
        country.save()

        return CreateCountry(
            id=country.id,
            country_name = country.country_name,
            geonameid = country.geonameid
        )

class Mutation(graphene.ObjectType):
    create_country = CreateCountry.Field()