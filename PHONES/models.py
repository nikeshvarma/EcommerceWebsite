from django.db import models

from PRODUCTS.models import Product


class PhoneDetails(models.Model):
    PHONE_TYPE = [
        ('Android', 'Android'),
        ('iPhone', 'iPhone'),
        ('Feature Phone', 'Feature Phone'),
        ('Tablet', 'Tablet')
    ]
    DISPLAY_TYPES = [
        ('IPS', 'IPS'),
        ('LCD', 'LCD'),
        ('AMOLED', 'AMOLED'),
        ('S-AMOLED', 'S-AMOLED'),
        ('RETINA', 'RETINA'),
        ('XDR', 'XDR'),
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=50, choices=PHONE_TYPE, default='Android')
    processor_name = models.CharField(max_length=100)
    RAM = models.PositiveIntegerField(default=1)
    internal_storage = models.PositiveIntegerField(default=32)
    color = models.CharField(max_length=50)
    display_size = models.CharField(max_length=20)
    display_resolution = models.CharField(max_length=20)
    display_type = models.CharField(max_length=50, choices=DISPLAY_TYPES, default='IPS')
    battery_capacity = models.PositiveIntegerField(default=3000)
    charger_output = models.CharField(max_length=6)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Phones'
