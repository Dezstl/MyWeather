from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Location
from django.template import Context, loader
import requests
from json import loads
from utils import WeatherByCityName


# Create your views here.

def home(request):
	cities = Location.objects.all()
	temp = WeatherByCityName('St. Louis')
	t = loader.get_template('weather/index.html')
	c = Context({'cities': cities, 'temp': temp,})
	return HttpResponse(t.render(c))

	
def apitest(request):
	response = WeatherByCityName('Saint Louis')
	
	t = loader.get_template('weather/display.html')
	c = Context({'weather': response,})
	return HttpResponse(t.render(c))