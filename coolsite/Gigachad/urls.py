from django.urls import path, include
from django.contrib import admin

from Gigachad.views import *

urlpatterns =[
    path('image/', image),
    path('', include('Gigachad.urls')),
    path('cats/', Category),
    path('number/<int:number>/', spisok),
    path("", index),

]

handler404 = pageNotFound