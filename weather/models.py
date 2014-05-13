from django.db import models

# Create your models here.

class Location(models.Model):
	cityName = models.CharField(max_length=200)
	cityID = models.CharField(max_length=20)
	lon = models.CharField(max_length=30)
	lat = models.CharField(max_length=30)
	
	def __str__(self):
	    return self.cityName + ' / ' + self.cityID + ' / ' + self.lat + ' / ' + self.lon