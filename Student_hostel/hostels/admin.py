from django.contrib import admin
from .models import Owner, Hostel, Room
from users.forms import CustomAuthenticationForm

# Register your models here.


class CustomAdminSite(admin.AdminSite):
    login_form = CustomAuthenticationForm
    site_header = "Student hostel"
    site_title = "Student hostel Administration"


admin_site = CustomAdminSite(name="myadmin")


class RoomInline(admin.StackedInline):
    model = Room
    extra = 3


class HostelAdmin(admin.ModelAdmin):
    list_display = ['name', "rep",
                    "total_number_of_rooms", "available_rooms", "average_room_price"]

    fieldsets = (
        (None, {
            "fields": (
                "name", "owner", "rep", "location"
            ),
        }),
    )
    inlines = [RoomInline]


admin_site.register(Owner)
admin_site.register(Hostel, HostelAdmin)
