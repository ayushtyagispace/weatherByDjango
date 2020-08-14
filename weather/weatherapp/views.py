from django.shortcuts import render
import json
import requests
import urllib.request
from the_weather.forms import CityForm
from the_weather.models import City
# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3f66010b91cfde119e547ebea1c261b0'
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()

    cities = City.objects.all()
    
    weather_data = []
    
    for city in cities:
            
        r = requests.get(url.format(city)).json() 
        
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'], 
        }
        weather_data.append(city_weather)

    context = {'weather_data':weather_data,'form':form}
    return render(request,'weather.html',context)