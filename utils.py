import urllib.request


def WeatherByCityName(name):
	baseUrl = 'http://api.openweathermap.org/data/2.5/weather?q='
	url = baseUrl + name
	
	response = urllib.request.urlopen(url)
	return response
	