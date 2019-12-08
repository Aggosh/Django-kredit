from django.urls import path

from .views import license, new


urlpatterns = [
    path('', new),
    path('license/', license),
]
