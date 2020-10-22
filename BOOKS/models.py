from django.db import models
from django.utils import timezone
from PRODUCTS.models import Product


class BookDetails(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    pages = models.CharField(max_length=6)
    publication_time = models.DateField(default=timezone.now)
    author = models.CharField(max_length=200)
    about_book = models.TextField()

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Books'
