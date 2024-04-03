from django.contrib import admin
from django.urls import path

from .views import views, search, list, create

urlpatterns = [   
    path("", views), 
    path('list/', list),
    path("searching/<name>", search),
    path('create/<name>/<service>', create)
]