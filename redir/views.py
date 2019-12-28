from django.shortcuts import redirect
from .models import Redirect


def my_redirect(request, compony_name):
    ref = Redirect.objects.get(title=compony_name)
    return redirect(ref.ref_url)
