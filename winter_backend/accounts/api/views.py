from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from ..models import User, UserAddress
from .serializers import UserSerializer, UserAddressSerializer


class UserViewSet(ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset"""


class UserAddressViewSet(ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer