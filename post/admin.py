from django.contrib import admin
from .models import Post, Advertising, Statistic, Review, Notification


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Advertising)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Statistic)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Notification)
class PostAdmin(admin.ModelAdmin):
    pass