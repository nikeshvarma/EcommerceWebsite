from django.contrib import admin
from .models import BookDetails


@admin.register(BookDetails)
class BookDetails(admin.ModelAdmin):
    pass
