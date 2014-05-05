from django.db import models

# Create your models here.

class Locations(models.Model):
	cityName = models.CharField(max_length=200)
	cityID = models.IntegerField()
	country = models.CharField(max length=200)
	lon = models.IntegerField()
	lat = models.IntegerField()
	
	def __str__(self):
	    return self.cityName + ' / ' + self.country + ' / ' + str(self.cityID) + ' / ' + str(self.lat) + ' / ' + str(self.lon)