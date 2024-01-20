from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Budget

class BudgetSerializer(ModelSerializer):
    class Meta:
        model = Budget
        verbose_name_plural = "categories"
        fields = ('user', 'name', 'start_date', 'end_date')