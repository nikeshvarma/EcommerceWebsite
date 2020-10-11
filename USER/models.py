from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserProfile(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER)
    delivery_address_1 = models.TextField(blank=True, null=True)
    delivery_address_2 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_user_profile'
