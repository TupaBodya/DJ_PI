from django.contrib import admin
from django.urls import path

from Gigachad.views import *

from django.urls import path

urlpatterns ={
    path('admin/', admin.site.urls),
    path('image/', image),
    path("", index),
    path('cats/<int:cats_id>/', Category),
    path('cats/<slug:cats>/', Category_slug),
    path('number/<int:number>/', spisok),
    path('test/', index32),
    path("year/<int:year>/", year_archive),
}

handler404 = pageNotFound