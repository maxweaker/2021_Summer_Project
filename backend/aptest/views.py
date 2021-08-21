from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, FileResponse
import simplejson
from prototype.models import Questionnaire,User
import django.utils.timezone as timezone
# Create your views here.
import os

def test1(request):
    if request.method == 'POST':
        print("s")
        path = os.path.dirname(__file__)

        r = simplejson.loads(request.body)
        userType = r['type']
        os.system("python D:\max\软工小学期\\backend\\amazing-qr-master\\amazing-qr-master\\amzqr.py https://baidu.com")
        #if userType in ['管理员','调度员']:
    return JsonResponse({"user":userType,"pic":'D:\max\软工小学期\\backend\qrcode.png'})

def test2(request):
    if request.method == 'POST':
        print("s1")
        file = open('D:\max\软工小学期\\backend\extest.xlsx', 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="extest.xlsx"'
        print(response)
        return response

def test3(request):
    if request.method == 'POST':
        print("s3")
        q = Questionnaire.objects.create(type=1,publishTime=timezone.now())
        u = User.objects.create(name='ling1',password='235')
        userType = 'u'
        return JsonResponse({"user": userType})