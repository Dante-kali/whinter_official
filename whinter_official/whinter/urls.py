from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("<h1>Hola, bienvenidos a mi aplicacion<h1>")

urlpatterns = [   
    path("", bienvenida),
]