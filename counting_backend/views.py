from calendar import month
from time import strftime
from tracemalloc import start
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime
from counting_backend.models import *
from django.views.decorators.csrf import csrf_exempt
from dateutil.relativedelta import relativedelta
from django.db.models import Q
# Create your views here.

COMSUME_TABLE = {
    "beauth":beauth,
    "clothes":clothes,
    "drinking":drinking,
    "eating":eating,
    "gift":gift,
    "health":health,
    "phonefee":phonefee,
    "save_money":save_money,
    "social":social,
    "sport":sport,
    "stock":stock,
    "taxing":taxing,
    "traffic":traffic,
    "utility_bill":utility_bill,
    }

@csrf_exempt
def insert_a_consume(request): # 記帳
    output_json = {
        "status":"",
        "error":""
    }
    consume_item = request.POST.get('consume_item')
    consume_price = request.POST.get('consume_price')
    consume_category = request.POST.get('consume_category')
    consume_date = request.POST.get('consume_date')
    if request:
        try:
            consume_date = datetime.datetime.strptime(consume_date,"%Y-%m-%d")
            consume.objects.create(consume_item = consume_item, consume_price = int(consume_price),consume_category = consume_category, consume_date = consume_date)
            COMSUME_TABLE[consume_category].objects.create(consume_item = consume_item, consume_price = int(consume_price), consume_date = consume_date)
            output_json['status'] = "success"
            return JsonResponse(output_json)
        except:
            output_json["status"] = "failed"
            output_json['error'] = "can't connect the db"
            return JsonResponse(output_json)
    output_json['error'] = "no data"
    output_json["status"] = "failed"
    return JsonResponse(output_json)

def get_date_segment(): # 計算發薪日至當前日期區段
    now_date = datetime.datetime.now()
    now_day = now_date.strftime("%d") # 獲取now的day做為start_day
    days_diff = abs(15 - int(now_day))
    if int(now_day) > 15: # 檢查day在15號之前後
        end_day = now_date - datetime.timedelta(days=days_diff)
    elif int(now_day) == 15: # 若目前日期剛好為15號
        end_day = now_date
    else: 
        end_day = now_date - relativedelta(months=1)
        end_day = end_day + datetime.timedelta(days=days_diff)
    return now_date,end_day

@csrf_exempt
def show_latest_month_consume(request): # 抓出目前日期到前一個發薪日的資料
    output_json = {
        "status":"",
        "consuming_data":[],
    }
    now_date,end_day = get_date_segment()
    if request.method == "GET":
        consume_data = list(consume.objects.filter(Q(consume_date__gte=end_day) & Q(consume_date__lte=now_date)).values())
        for number,temper in enumerate(consume_data):
            current_month_consumeing = {
                "consume_item":consume_data[number]['consume_item'],
                "consume_price":consume_data[number]['consume_price'],
                "consume_category":consume_data[number]['consume_category'],
                "consume_date":consume_data[number]['consume_date'],
            }
            output_json["consuming_data"].append(current_month_consumeing)
        output_json["status"] = "success"
    return JsonResponse(output_json)

@csrf_exempt
def show_category_consume(request): # 抓出依照類別的消費，日期可不代入
    output_json = {
        "status":"",
        "consuming_data":[],
    }
    current_month_consumeing = {
        "consume_item":"",
        "consume_price":"",
        "consume_date":"",
    }
    consume_category = request.POST.get('consume_category')
    consume_date = request.POST.get('consume_date',None)
    now_date,end_day = get_date_segment()
    if request.method == "POST":
        if consume_date == None:
            consume_data = list(COMSUME_TABLE[consume_category].objects.all().values())
            for number,temper in enumerate(consume_data):
                current_month_consumeing["consume_item"] = consume_data[number]['consume_item'],
                current_month_consumeing["consume_price"] = consume_data[number]['consume_price'],
                current_month_consumeing["consume_date"] = consume_data[number]['consume_date'],
                output_json["data"].append(current_month_consumeing)
            output_json["status"] = "success"
        elif consume_date !=None: # 有代入日期
            consume_data = list(COMSUME_TABLE[consume_category].objects.filter(Q(consume_date__gte=end_day) & Q(consume_date__lte=now_date)).values())
            for number,temper in enumerate(consume_data):
                current_month_consumeing["consume_item"] = consume_data[number]['consume_item'],
                current_month_consumeing["consume_price"] = consume_data[number]['consume_price'],
                current_month_consumeing["consume_date"] = consume_data[number]['consume_date'],
                output_json["data"].append(current_month_consumeing)
            output_json["status"] = "success"
        else:
            output_json["status"] = "failed"
    return JsonResponse(output_json)
        