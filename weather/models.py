from django.db import models

# Create your models here.

class Locations(models.Model):
	cityName = models.CharField(max_length=200)
	cityID = models.IntegerField()
	lon = models.IntegerField()
	lat = models.IntegerField()
	
	def __str__(self):
	    return self.cityName + ' / ' + str(self.cityID) + ' / ' + str(self.lat) + ' / ' + str(self.lon)