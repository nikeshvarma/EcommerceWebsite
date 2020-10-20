from django.contrib import admin
from .models import Order, TransactionDetails


@admin.register(Order)
class Orders(admin.ModelAdmin):
    list_display = ['order_id', 'name', 'phone_number', 'order_date', 'order_status']


@admin.register(TransactionDetails)
class TransactionDetails(admin.ModelAdmin):
    pass
