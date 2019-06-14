from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    geonameid = models.IntegerField()

    def __str__(self):
        return "{}/{}".format(self.country_name, self.geonameid)

class SubCountry(models.Model):
    subcountry_name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.subcountry_name)

class City(models.Model):
    city_name = models.CharField(max_length=50)
    subcountry = models.ForeignKey(SubCountry, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.city_name)


    
