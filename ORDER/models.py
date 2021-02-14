from django.db import models
from django.contrib.auth import get_user_model
from PRODUCTS.models import Product
from SELLER.models import Shop

User = get_user_model()


class Order(models.Model):
    ORDER_STATUS = [
        ('Approved', 'Approved'),
        ('Packed', 'Packed'),
        ('Dispatched', 'Dispatched'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
        ('Failed', 'Failed'),
    ]

    order_id = models.AutoField(primary_key=True, unique=True, verbose_name='order_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_seller': False})
    product = models.ManyToManyField(Product, through='ProductOrdered')
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    amount = models.FloatField()
    address = models.TextField()
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=30)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='Ordered')

    def __str__(self):
        return str(self.order_id)

    class Meta:
        db_table = 'tbl_orders'
        ordering = ['-order_id']


class ProductOrdered(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=1)

    def __str__(self):
        return str(self.order.order_id)

    class Meta:
        db_table = 'tbl_order_product'


class TransactionDetails(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=128)
    bank_transaction_id = models.CharField(max_length=128)
    transaction_amount = models.CharField(max_length=100)
    transaction_status = models.CharField(max_length=200)
    transaction_type = models.CharField(max_length=200)
    gateway_name = models.CharField(max_length=200)
    response_code = models.CharField(max_length=200)
    response_message = models.TextField()
    bank_name = models.CharField(max_length=200)
    payment_mode = models.CharField(max_length=200)
    refund_amount = models.CharField(max_length=100)
    transaction_date = models.CharField(max_length=200)

    class Meta:
        db_table = 'tbl_transaction_details'
