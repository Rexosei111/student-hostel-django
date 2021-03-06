from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.


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

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Hostel(models.Model):
    name = models.CharField(max_length=20, null=True, unique=True, blank=False)
    owner = models.OneToOneField(
        Owner, on_delete=models.CASCADE, related_name="owner")
    rep = models.OneToOneField(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'is_staff': True})
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def available_rooms(self):
        return self.rooms.filter(occupied=False).count()

    def average_room_price(self):
        average_price = self.rooms.aggregate(models.Avg('price'))
        return average_price['price__avg']

    def total_number_of_rooms(self):
        return self.rooms.count()


class Room(models.Model):
    number = models.IntegerField()
    hostel_name = models.ForeignKey(
        Hostel, on_delete=models.CASCADE, related_name="rooms")
    number_of_occupants = models.IntegerField()
    size = models.CharField(max_length=20, null=True, blank=True)
    occupied = models.BooleanField(default=False, blank=False)
    price = models.FloatField(blank=False)

    class Meta:
        ordering = ['hostel_name']

    def __str__(self):
        return f"{self.hostel_name} {self.number}"

    def save(self, *args, **kwargs):
        if (self.occupants.count() > self.number_of_occupants):
            raise ValueError(_(
                f"Number of occupants of this room cannot be more than {self.number_of_occupants}"))

        if (self.occupants.count() == self.number_of_occupants):
            self.occupied = True

        if (self.number == None):
            self.number = self.hostel_name.rooms.count() + 1

        super().save(*args, **kwargs)
