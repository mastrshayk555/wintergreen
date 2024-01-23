from .forms import RegisterForm, PasswordResetForm, SetPasswordForm
from .models import User
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.views.generic import DetailView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.views import PasswordResetConfirmView

# Create your views here.

class Register(DetailView):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):

        template = 'accounts/register.html'

        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'That email already exists. Try another or click below to recover your password.'
                })
            else:
                user = User.objects.create_user(
                    email = form.cleaned_data['email'],
                    first_name = form.cleaned_data['first_name'],
                    last_name = form.cleaned_data['last_name'],
                    phone = form.cleaned_data['phone_number'],
                    password = form.cleaned_data['password'],
                )
                user.save()
        return render(request, template, {
                    'form': form,
                    'error_message': 'NOthing yet.'
                })
    

class SignIn(DetailView):
    def get(self, request):
        return render(request, 'accounts/sign_in.html')
    

class PasswordReset(DetailView):    
    def get(self, request):
        form = PasswordResetForm()
        return render(
            request, 
            'accounts/reset_password.html',
            {'form': form}
        )
