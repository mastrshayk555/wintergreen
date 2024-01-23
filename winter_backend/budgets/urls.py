from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

app_name = "budgets"
urlpatterns = [
    path(
        'user-home/', 
        views.BudgetHome.as_view(), 
        name='user-home'
    ),
    path(
        'logout',
        views.UserLogout.as_view(),
        name='logout'
    )
]