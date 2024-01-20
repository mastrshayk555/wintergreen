from django.urls import include, path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('login', views.SignIn.as_view(), name='login'),
]
