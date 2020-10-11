from django.db import models
from PRODUCTS.models import Product


class LaptopDetails(models.Model):
    LAPTOP_TYPE = [
        ('Notebook', 'Notebook'),
        ('Chromebook', 'Chromebook'),
        ('MacBook', 'MacBook'),
        ('Gaming Laptop', 'Gaming Laptop')
    ]
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    laptop_type = models.CharField(max_length=50, choices=LAPTOP_TYPE)
    RAM = models.IntegerField(default=1)
    hdd = models.IntegerField(default=32)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Laptop'
