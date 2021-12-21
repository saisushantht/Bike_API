from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from appli.models import Bike

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_bike(request,bike_name):
    if request.method == 'GET':
        try:
            bike = Bike.objects.get(name=bike_name)
            response = json.dumps([{'Bike':bike.name,'Top Speed':bike.top_speed}])
        except:
            response = json.dumps([{'Error':'No Bike with that name'}])

    return HttpResponse(response,content_type='text/json')


@csrf_exempt
def add_bike(request):
    print(request.body)
    print( "      ------------------====")
    if request.method == 'POST':
        payload = json.loads((request.body))
        print(payload)
        bike_name = payload['bike_name']
        top_speed = payload['top_speed']
        bike = Bike(name=bike_name, top_speed=top_speed)
        try:
            bike.save()
            response = json.dumps([{'Success':'Bike added successfully !!!'}])
        except:
            response = json.dumps([{'Error':'Bike could not be added'}])

    return HttpResponse(response,content_type='text/json')
