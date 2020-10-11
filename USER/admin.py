from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class Profiles(admin.ModelAdmin):
    pass
