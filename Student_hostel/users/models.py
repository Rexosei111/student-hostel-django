from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.conf import settings


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email Address", unique=True)
    index_number = models.CharField(max_length=12, unique=True)

    USERNAME_FIELD = 'index_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.index_number


class Owner(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = models.CharField(max_length=15, null=True, blank=False)
    last_name = models.CharField(max_length=15, null=True, blank=False)
    phone_number = models.CharField(max_length=13, null=True, blank=False)
    email_address = models.EmailField(
        verbose_name="Email Address", null=True, blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=6, null=True,
                              blank=False, choices=GENDER)
    residence = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Hostel(models.Model):
    name = models.CharField(max_length=20, null=True, unique=True, blank=False)
    owner = models.OneToOneField(Owner, on_delete=models.CASCADE)
    manager = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_staff': True})
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
