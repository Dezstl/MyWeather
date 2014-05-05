from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Locations
from django.template import Context, loader

# Create your views here.

def home(request):
	cities = Locations.objects.all()
	t = loader.get_template('weather/index.html')
	c = Context({'cities': cities,})
	return HttpResponse(t.render(c))
