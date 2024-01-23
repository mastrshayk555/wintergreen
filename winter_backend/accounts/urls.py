from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

app_name = "accounts"
urlpatterns = [
    path(
        'register', 
        views.Register.as_view(), 
        name='register'
    ),
    path(
        'accounts/login/', 
        auth_views.LoginView.as_view(
            template_name = 'registration/login.html',
        ),
        name = 'login'
    ),
    path(
        'reset_password', 
        views.PasswordReset.as_view(), 
        name='reset_password'
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name = 'accounts/password_reset_confirm.html',
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name = 'accounts/password_reset_done.html',
        ),
        name='password_reset_done'
    ),

]
