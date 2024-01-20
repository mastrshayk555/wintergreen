from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserAddress, UserProfile
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from accounts.models import User
# Register your models here.

class CusomterCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data("password1")
        password2 = self.cleaned_data("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed formats
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "is_active", "is_admin"]

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = CusomterCreationForm


    list_display = ["email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {'fields': ["email", "password"]}),
        ("Personal Info", {"fields": ["first_name", "last_name", "date_created"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "date_of_birth", "password1", "password2"],
            },
        )
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []
    readonly_fields = ["date_created"]

@admin.display(description="Name")
def full_name(obj):
    print(obj)
    return f"{obj.first_name} {obj.last_name}"
    

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "address_one"
    )
    fields = [
        "address_type",
        "user",
        "address_one",
        "address_two",
        "city",
        "state",
        "zipcode",
    ]

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_of_birth",
        "industry",
        "job_title",
    )