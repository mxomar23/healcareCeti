from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User

from .models import Paciente


class Uswer(admin.ModelAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username',)
    list_filter = ('is_staff', 'is_superuser', 'date_joined')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Informacion personal', {'fields': ('first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_superuser', 'is_staff', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()



admin.site.register(Paciente)
admin.site.unregister(Group)
