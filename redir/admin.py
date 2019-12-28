from django.contrib import admin
from .models import Redirect


@admin.register(Redirect)
class PostAdmin(admin.ModelAdmin):
    pass
