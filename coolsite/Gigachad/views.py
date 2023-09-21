#Модуль для хранения представлений приложения
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Привет, Мужички") and HttpResponse("Привет, лошки <img src=https://avatars.mds.yandex.net/get-verba/787013/2a0000016b7e65c13c5acad18b2101595da2/cattouchret>")

def Category(request, cats_id):
    return HttpResponse(f"<h1> статья под номером {cats_id} </h1>")

def index1(request):
    return HttpResponse("Пока, Мужички")
def image(request):
    return HttpResponse("<img src=https://avatars.mds.yandex.net/get-verba/787013/2a0000016b7e65c13c5acad18b2101595da2/cattouchret>")
def Category_slug(request, cats):
    return HttpResponse(f"<h1> статья под категорией {cats} </h1>")