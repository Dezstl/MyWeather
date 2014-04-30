from django.shortcuts import render
from django.http import HttpResponse
from weather.models import Locations

# Create your views here.

def home(request):
	cities = Locations.objects.all()
	return HttpResponse(cities)
