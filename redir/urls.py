from django.urls import path

from .views import my_redirect


urlpatterns = [
    path('<str:compony_name>', my_redirect),
]
