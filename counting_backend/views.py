from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime
from counting_backend.models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def hello(request):
    ccc = request.POST.get('username')
    bbb = request.POST.get('password')
    output_json = {
        "status":"success",
        "data":"",
        "user":"",
        "password":""
    }
    aaa = list(eating.objects.all().values())
    output_json['data'] = aaa
    output_json['user'] = ccc
    output_json['password'] = bbb
    return JsonResponse(output_json) 
@csrf_exempt
def insert_a_consume(request):
    output_json = {
        "status":"",
        "data":""
    }
    consume_item = request.POST.get('consume_item')
    consume_price = request.POST.get('consume_price')
    consume_category = request.POST.get('consume_category')
    consume_date = request.POST.get('consume_date')
    
    return JsonResponse(output_json)