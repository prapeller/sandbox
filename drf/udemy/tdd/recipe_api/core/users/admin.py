from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = (
        (_('Credentials'), {'fields': ('email', 'username')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (_('Credentials'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


admin.site.register(models.User, UserAdmin)
