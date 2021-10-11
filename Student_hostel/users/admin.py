from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm
from .models import User
from django.contrib.auth.models import Group


class CustomAdminSite(admin.AdminSite):
    login_form = CustomAuthenticationForm


admin_site = CustomAdminSite(name="myadmin")


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('index_number', 'email', 'is_superuser',
                    'is_staff', 'is_active',)
    list_filter = ('index_number', 'email', 'is_superuser',
                   'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('index_number', 'email', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('index_number', 'email', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('index_number', 'email',)
    ordering = ('index_number', 'email',)


admin_site.register(User, CustomUserAdmin)
admin_site.register(Group)
