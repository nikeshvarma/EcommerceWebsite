from django.contrib import admin
from .models import (
    Shop,
    ShopOwnerBankDetails
)


@admin.register(Shop)
class Shops(admin.ModelAdmin):
    pass


@admin.register(ShopOwnerBankDetails)
class BankDetails(admin.ModelAdmin):
    pass
