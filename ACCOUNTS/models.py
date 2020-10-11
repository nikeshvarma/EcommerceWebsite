from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.utils.translation import ugettext_lazy as _


class AuthUser(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_seller = models.BooleanField(default=False)
    is_verified_seller = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'auth_user'
