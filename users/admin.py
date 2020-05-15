# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    add_form = CustomUserCreationForm
    add_fieldsets = (
                     (None, {
                      'classes': ('wide',),
                      'fields': ('username', 'email', 'is_staff', 'first_name', 'last_name', 'groups', 'password1', 'password2')}
                      ),
                     )

    form = CustomUserChangeForm
    fieldsets = (
                     (None, {
                      'classes': ('wide',),
                      'fields': ('username', 'email', 'is_staff', 'first_name', 'last_name', 'groups', 'password')}
                      ),
                     )
    model = CustomUser
    # The fields to be used in displaying the User model.
    list_display = ['username', 'email', 'first_name', 'last_name',  'is_staff', 'is_active', 'date_joined']


admin.site.register(CustomUser, CustomUserAdmin)
