from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Locations
from django.template import Context, loader
import requests
import json 
from utils import WeatherByCityName


# Create your views here.

def home(request):
	cities = Locations.objects.all()
	t = loader.get_template('weather/index.html')
	c = Context({'cities': cities,})
	return HttpResponse(t.render(c))

	
def apitest(request, city):
	response = WeatherByCityName(city)
	return HttpResponse(response)