from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Shop(models.Model):
    shop_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=150)
    shop_email_address = models.EmailField(null=True, blank=True)
    shop_phone_number = models.CharField(max_length=13)
    shop_address = models.TextField()
    area_pincode = models.CharField(max_length=6)
    shop_state = models.CharField(max_length=200)
    shop_city = models.CharField(max_length=200)
    shop_description = models.TextField(null=True, blank=True)
    is_shop_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.shop_name

    class Meta:
        db_table = 'tbl_registered_shops'


class ShopOwnerBankDetails(models.Model):
    shop_owner = models.OneToOneField(Shop, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=20)
    IFSC_code = models.CharField(max_length=11)
    PAN_number = models.CharField(max_length=11)

    def __str__(self):
        return str(self.shop_owner)

    class Meta:
        db_table = 'tbl_shop_owner_bank_details'
