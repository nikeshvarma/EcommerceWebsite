from django.contrib import admin
from .models import AuthUser


@admin.register(AuthUser)
class Accounts(admin.ModelAdmin):
    list_display = ('email', 'is_seller', 'is_active', 'last_login')
