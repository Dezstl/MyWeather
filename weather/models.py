from django.db import models

# Create your models here.

class Locations(models.Model):
	cityName = models.CharField(max_lenght=200)
	cityID = models.IntegerField()
	lon = models.CharField()
	lat = modles.IntegerField()
