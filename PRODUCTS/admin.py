from django.contrib import admin
from .models import (
    Category,
    ProductType,
    Product
)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['category_name']


@admin.register(ProductType)
class ProductType(admin.ModelAdmin):
    list_display = ['category', 'product_type']


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['product_name', 'product_stoke', 'product_MRP', 'is_product_live', 'is_product_verified', 'product_shop']
    list_per_page = 20
