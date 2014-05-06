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

	
def apitest(request):
	try:
		u = "http://api.openweathermap.org/data/2.5/weather?q={0}&units={1}"
		r = requests.get(u.format(loc, units))
		j = json.loads(r.text)
	except:
		sys.stderr.write("Couldn't load current conditions\n")
	
	return HttpResponse(j)