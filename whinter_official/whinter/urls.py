from django.contrib import admin
from django.urls import path

from .views import views, search

urlpatterns = [   
    path("", views),
    path("searching/<name>", search)
] 