from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from ..models import User, UserAddress

User = get_user_model()


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'username',
            'email',
            'username',
            'password'
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'phone',
            'email',
            'date_created',
        )


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = (
            'user',
            'address_one',
            'address_two',
            'city',
            'state',
            'zipcode',
        )