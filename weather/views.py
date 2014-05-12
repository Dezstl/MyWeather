from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Locations
from django.template import Context, loader
import requests
from json import loads
from utils import WeatherByCityName


# Create your views here.

def home(request):
	cities = Locations.objects.all()
	temp = WeatherByCityName('Chicago')
	t = loader.get_template('weather/index.html')
	c = Context({'cities': cities, 'temp': temp,})
	return HttpResponse(t.render(c))

	
def apitest(request):
	response = WeatherByCityName('Chicago')
	
	t = loader.get_template('weather/display.html')
	c = Context({'weather': response,})
	return HttpResponse(t.render(c))