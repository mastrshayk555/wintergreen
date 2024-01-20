from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserAddressViewSet


user_router = DefaultRouter()
user_router.register(r'user', UserViewSet, basename='user')

user_address_router = DefaultRouter()
user_address_router.register(r'useraddress', UserAddressViewSet)

