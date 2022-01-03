from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username', 'is_active', 'is_staff', 'is_superuser']
    fieldsets = (
        (_('Credentials'), {'fields': ('email', 'username')}),
        (_('Status'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Permissions'), {'fields': ('user_permissions',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('Track dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (_('Credentials'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')
        }),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )


admin.site.register(get_user_model(), UserAdmin)