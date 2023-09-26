#Модуль для хранения представлений приложения
from django.http import HttpResponse, HttpResponseNotFound, Http404
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
def spisok(request,number):
    dir={
        "1":['Король Б.А 22.08.2002'],
        "2":['Игнатьев А.А 28.06.2001'],
        "3":['Лелетко П.А 19.03.2004'],
        "4":['Снытко Г.А 28.10.2004'],
        "5":['Мартыненко Ю.А 11.03.2004'],
        "6":['Селебин А.Б 11.02.2004'],
        "7": ['Тузов А.С 16.06.2004'],
        "8": ['Ковалёв Р.С 13.06.2004'],
        "9": ['Коновалов А.Е. 12.06.2004'],
        "10": ['Сердюков А.С 17.06.2004'],
        }
    if number > 0 and number <10:
        return HttpResponse(f"<h1> Студент {dir[str(number)][0]} найден </h1>")
    else:
        return HttpResponse(f"<h1> Студента под номером {number} не найден </h1>")
def index32(request):
    print(request.GET)
    return HttpResponse(f"Страница приложения Gigachad{dict(request.GET)}")

def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Ошибка 404, попробуйте ещё раз<br>{exception}</h1>")

def year_archive(request,year):
        if(int(year))>2023:
            raise Http404()
        return HttpResponse(f"<h1> Год издания {year}</h1>")