from django.urls import path

from .views import license, new, about


urlpatterns = [
    path('', new),
    path('license/', license),
    path('about/', about),
]
