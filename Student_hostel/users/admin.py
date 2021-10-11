from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


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


admin.site.register(User, CustomUserAdmin)
