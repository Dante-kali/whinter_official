from django.contrib import admin
from django.urls import path

from .views import views, search, selection, create

urlpatterns = [   
    path("", views),
    path('selection/', selection),
    path("searching/<name>", search),
    path('create/<name>/<service>', create)
]