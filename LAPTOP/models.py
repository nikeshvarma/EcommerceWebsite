from django.db import models
from PRODUCTS.models import Product


class LaptopDetails(models.Model):
    LAPTOP_TYPE = [
        ('Notebook', 'Notebook'),
        ('Chromebook', 'Chromebook'),
        ('MacBook', 'MacBook'),
        ('Gaming Laptop', 'Gaming Laptop')
    ]

    OS = [
        ('Windows', 'Windows'),
        ('MAC-OS', 'MAC-OS'),
        ('Linux', 'Linux'),
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    laptop_type = models.CharField(max_length=50, choices=LAPTOP_TYPE)
    processor_name = models.CharField(max_length=100)
    graphic_card_name = models.CharField(max_length=200)
    RAM = models.PositiveIntegerField(default=4)
    HDD = models.CharField(max_length=6)
    SSD = models.CharField(max_length=6)
    charger_output = models.CharField(max_length=6)
    has_graphic_card = models.BooleanField(default=False)
    operating_system = models.CharField(max_length=100, choices=OS)
    warranty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Laptop'
        db_table = 'tbl_laptop_details'
