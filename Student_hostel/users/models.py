from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email Address", unique=True)
    index_number = models.CharField(max_length=12, unique=True)

    USERNAME_FIELD = 'index_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.index_number
