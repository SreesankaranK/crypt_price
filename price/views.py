from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
def index(request):
    response = requests.get("https://api.coinmarketcap.com/v2/ticker/")
    json_data = response.json()
    data=json_data.get('data',[])
   
   
    template = loader.get_template("index.html")
    
    return HttpResponse(template.render({'data':data}))

# Create your views here.
    