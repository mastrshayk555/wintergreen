from rest_framework.routers import DefaultRouter
from budgets.api.urls import budget_router
from accounts.api.urls import user_router, user_address_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(budget_router.registry)
router.registry.extend(user_router.registry)
router.registry.extend(user_address_router.registry)


urlpatterns = [
    path('', include(router.urls))
]
