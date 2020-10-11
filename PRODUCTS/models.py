from django.db import models

from SELLER.models import Shop


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'tbl_product_category'


class ProductType(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100)

    def __str__(self):
        return self.product_type

    class Meta:
        db_table = 'tbl_product_type'


class Product(models.Model):
    product_shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_stoke = models.IntegerField()
    product_MRP = models.IntegerField()
    product_selling_price = models.IntegerField()
    product_home_img = models.ImageField(upload_to='products_homepage_images')
    is_product_live = models.BooleanField(default=False)
    is_product_verified = models.BooleanField(default=False)
    product_add_datetime_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_name)

    class Meta:
        db_table = 'tbl_product'
        ordering = ['-id']
