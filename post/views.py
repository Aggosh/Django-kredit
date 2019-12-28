from django.shortcuts import render
from .base_context import make_base_context


def license(request):
    return render(request, 'license.html')


def about(request):
    return render(request, 'about.html')


def new(request):
    cont = make_base_context()
    return render(request, 'new_base.html', context=cont)


def question(request):
    return render(request, 'question.html')


def error_404_view(request, exception):
    return render(request, 'error_404.html')


def error_500_view(request):
    return render(request, 'error_500.html')
