import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from country_list.schema.query.city import CityType
from country_list.models import Country, City

from country_list.utils.read_country import FindCountry 

class CountryType(DjangoObjectType):
    class Meta:
        model = Country


class Query(graphene.ObjectType):
    countries = graphene.List(CountryType, country=graphene.String())
    cities = graphene.List(CityType)

    def resolve_countries(self, info, **kwargs):
        if kwargs.get('country'):
            country = kwargs.pop('country')
            filter = Q(country_name__icontains=country)
            return Country.objects.filter(filter)
        else:
            fc = FindCountry()
            fc.add_country(country)
        return Country.objects.all()

    def resolve_cities(self, info, **kwargs):
        return City.objects.all()

