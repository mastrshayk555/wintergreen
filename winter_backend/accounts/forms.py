from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget, RegionalPhoneNumberWidget

class RegisterForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control", "style": "color:black;"}), required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control", "style": "color:black;"}), required=True)
    password_repeat = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control", "style": "color:black;"}), required=True)
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "style": "color:black;"}), required=False)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control", "style": "color:black;"}), required=False)
    phone_number = PhoneNumberField(
        widget = RegionalPhoneNumberWidget(
            region="US",
            attrs={
                "class": "form-control", 
                "style": "color:black;"
            }
        )
    )
