from django.shortcuts import render
from .base_context import make_base_context


def license(request):
    cont = make_base_context()

    return render(request, 'license.html', context=cont)


def new(request):
    cont = make_base_context()

    return render(request, 'new_base.html', context=cont)
