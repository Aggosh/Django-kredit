from django.urls import path

from .views import license, new, about, question


urlpatterns = [
    path('', new),
    path('license/', license),
    path('about/', about),
    path('question/', question),
]
