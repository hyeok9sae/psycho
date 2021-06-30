from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import datetime, timedelta, date
from .models import *
from .serializers import *
import json

# Create your views here.
'''
요청example
{
    "syear": 2020,
    "smonth": 9,
    "sday": 4,
    "eyear": 2020,
    "emonth": 9,
    "eday": 4,
    "gubun": "남"
}
'''


@csrf_exempt
def getCovid19Info(request):
    if request.method == 'GET':
        data = Covid19Info.objects.all()
        serializer = Covid19InfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        param = json.loads(request.body)

        start = date(param['syear'], param['smonth'], param['sday'])
        end = date(param['eyear'], param['emonth'], param['eday'])
        end = end + timedelta(days=1)

        data = Covid19Info.objects.filter(createDt__range=(start, end))
        serializer = Covid19InfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def getCovid19GenAgeInfo(request):
    if request.method == 'GET':
        data = Covid19GenAgeInfo.objects.all()
        serializer = Covid19GenAgeInfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        param = json.loads(request.body)

        start = date(param['syear'], param['smonth'], param['sday'])
        end = date(param['eyear'], param['emonth'], param['eday'])
        end = end + timedelta(days=1)

        data = Covid19GenAgeInfo.objects.filter(
            createDt__range=(start, end), gubun__icontains=param['gubun'])
        serializer = Covid19GenAgeInfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def getCovid19SidoInfo(request):
    if request.method == 'GET':
        data = Covid19SidoInfo.objects.all()
        serializer = Covid19SidoInfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    elif request.method == 'POST':
        param = json.loads(request.body)

        start = date(param['syear'], param['smonth'], param['sday'])
        end = date(param['eyear'], param['emonth'], param['eday'])
        end = end + timedelta(days=1)

        data = Covid19SidoInfo.objects.filter(
            createDt__range=(start, end), gubun__icontains=param['gubun'])
        serializer = Covid19SidoInfoSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
