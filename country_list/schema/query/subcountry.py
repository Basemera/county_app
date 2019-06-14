import graphene
from graphene_django import DjangoObjectType

from country_list.models import SubCountry

class SubCountryType(DjangoObjectType):
    class Meta:
        model = SubCountry


class Query(graphene.ObjectType):
    subcountries = graphene.List(SubCountryType)

    def resolve_subcountries(self, info, **kwargs):
        return SubCountry.objects.all()