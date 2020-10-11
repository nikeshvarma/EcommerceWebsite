from django.db import models

from PRODUCTS.models import Product


class PhoneDetails(models.Model):
    PHONE_TYPE = [
        ('Android', 'Android'),
        ('iPhone', 'iPhone'),
        ('Feature Phone', 'Feature Phone'),
        ('Tablet', 'Tablet')
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    phone_type = models.CharField(max_length=50, choices=PHONE_TYPE)
    RAM = models.IntegerField(default=1)
    internal_storage = models.IntegerField(default=32)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Phones'
