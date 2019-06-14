import json
import os
from django.db.models import ObjectDoesNotExist
from django.db.utils import IntegrityError
from country_list.models import Country, SubCountry, City

class FindCountry:
    def __init__(self):
        self._dir_name = os.path.dirname(os.path.abspath(__file__))

        # read
        with open(self._dir_name + '/countries.json', 'r') as self.countries_file:
            self._data = self.countries_file.read()

        # parse
        self.countries = json.loads(self._data)


    def add_country(self, input_country):
        # first check database to see if country exists if not search json file and add its relate details
        try:
            Country.objects.get(country_name=input_country)
            print("Country already exists")
        except ObjectDoesNotExist: 
            for item in self.countries:
                if item['country'] == input_country:
                    try:
                        self.country = Country.objects.create(country_name=item['country'], geonameid=item['geonameid'])
                        self.country.save()
                    except IntegrityError:
                        # save the subcountry as a subset of the country
                        self.subcountry = self.country.subcountry_set.create(subcountry_name=item['subcountry'])
                        self.subcountry.save()
                        # save the city a a subset of resulting subcoutry
                        self.city = self.subcountry.city_set.create(city_name=item['name'])
                        self.city.save()

