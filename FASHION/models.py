from django.db import models

from PRODUCTS.models import Product


class ShirtDetails(models.Model):
    SHIRT_SIZES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('2XL', '2XL'),
    ]

    FITTING_TYPES = [
        ('Regular', 'Regular'),
        ('Loose', 'Loose'),
        ('Fit', 'Fit'),
    ]

    SLEEVE_TYPE = [
        ('Full', 'Full'),
        ('Half', 'Half'),
    ]

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices=SHIRT_SIZES)
    fitting_type = models.CharField(max_length=50, choices=FITTING_TYPES)
    color = models.CharField(max_length=50)
    fabric = models.CharField(max_length=50)
    sleeve = models.CharField(max_length=50, choices=SLEEVE_TYPE)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name_plural = 'Shirts'
        db_table = 'tbl_shirt_details'
