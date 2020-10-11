from django.contrib import admin
from .models import PhoneDetails


@admin.register(PhoneDetails)
class PhoneDetails(admin.ModelAdmin):
    pass
