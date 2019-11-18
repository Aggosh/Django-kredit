from django.contrib import admin
from django.urls import path

from .views import index, license, reviews, new


urlpatterns = [
    path('', index),
    path('license/', license),
    path('new/', new),
    path('reviews/', reviews),
]
