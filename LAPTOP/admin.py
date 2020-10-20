from django.contrib import admin
from .models import LaptopDetails


@admin.register(LaptopDetails)
class LaptopDetails(admin.ModelAdmin):
    pass
