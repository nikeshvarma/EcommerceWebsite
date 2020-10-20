from django.contrib import admin
from .models import ShirtDetails


@admin.register(ShirtDetails)
class ShirtDetails(admin.ModelAdmin):
    pass
