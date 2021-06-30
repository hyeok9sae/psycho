from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import sns.morph as morph
# Create your views here.

@csrf_exempt
def sns_make(request):
    if request.method == 'GET':
        exec(open(morph).read())
        return HttpResponse('<h1>success</h1>')