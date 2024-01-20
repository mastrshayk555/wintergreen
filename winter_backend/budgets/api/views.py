from ..models import Budget
from .serializers import BudgetSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class BudgetViewSet(ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetViews(APIView):
    def get(self, request):
        print(request.GET.get('username'))
        return Response()