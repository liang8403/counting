from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime
from counting_backend.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def hello(request):
    ccc = request.POST['username']
    bbb = request.POST['password']
    output_json = {
        "status":"success",
        "data":"",
        "user":"",
        "password":""
    }
    print(request.POST)
    aaa = list(eating.objects.all().values())
    output_json['data'] = aaa
    output_json['user'] = ccc
    output_json['password'] = bbb
    return JsonResponse(output_json) 
def insert_a_consume(request):
    return True