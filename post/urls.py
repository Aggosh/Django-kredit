from django.contrib import admin
from django.urls import path

from .views import index, license, reviews


urlpatterns = [
    path('', index),
    path('license/', license),
    path('reviews/', reviews),
]
