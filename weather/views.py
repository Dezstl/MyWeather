from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Locations
from django.template import Context, loader
import requests
import json 


# Create your views here.

def home(request):
	cities = Locations.objects.all()
	t = loader.get_template('weather/index.html')
	c = Context({'cities': cities,})
	return HttpResponse(t.render(c))

	
def apitest(request):
	
	u = "http://api.openweathermap.org/data/2.5/find?q=London&mode=json"
	r = requests.get(u)
	j = json.loads(r.text)
	
	
	return HttpResponse(r)