import json
import requests


def WeatherByCityName(name):
	baseUrl = 'http://api.openweathermap.org/data/2.5/weather?'
		
	params = {'q': name, 'units': 'imperial'}
	
	resp = requests.get(url=baseUrl, params=params).json()
	
	return resp