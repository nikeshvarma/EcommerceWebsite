from django.contrib import admin
from .models import CarouselImage


@admin.register(CarouselImage)
class CarouselIMG(admin.ModelAdmin):
    pass
