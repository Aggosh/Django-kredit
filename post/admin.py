from django.contrib import admin
from .models import Compony, Advertising, Review, Notification


@admin.register(Compony)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Advertising)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class PostAdmin(admin.ModelAdmin):
    pass