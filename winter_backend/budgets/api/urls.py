from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, BudgetViews


budget_router = DefaultRouter()
budget_router.register(r'budget', BudgetViewSet)

#urlpatterns = [
#    path('budgets/', BudgetViews.as_view(), name='budgets')
#    #path("budgets_again/",  )
#]
