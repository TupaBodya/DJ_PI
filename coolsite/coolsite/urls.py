from django.contrib import admin
from django.urls import path

from Gigachad.views import *

urlpatterns ={
    path('admin/', admin.site.urls),
    path('image/', image),
    path("", index),
    path('cats/<int:cats_id>/', Category),
    path('cats/<slug:cats>/', Category_slug),
}