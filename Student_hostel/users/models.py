from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager
from django.conf import settings
from hostels.models import Hostel, Room
from .utils import normalize_index_number


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Email Address", unique=True)
    index_number = models.CharField(max_length=12, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    hostel_name = models.ForeignKey(
        Hostel, on_delete=models.SET_NULL, null=True, blank=True, to_field="name", related_name="students")
    room_number = models.ForeignKey(
        Room, on_delete=models.SET_NULL, null=True, blank=True, related_name="occupants")

    USERNAME_FIELD = 'index_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def save(self, *args, **kwargs):
        index_number = normalize_index_number(self.index_number)
        self.index_number = index_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.index_number
