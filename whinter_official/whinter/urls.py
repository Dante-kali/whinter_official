from django.contrib import admin
from django.urls import path

from .views import views, search, selection

urlpatterns = [   
    path("", views),
    path('selection/', selection),
    path("searching/<name>", search)
] 