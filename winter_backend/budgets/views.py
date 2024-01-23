from django.shortcuts import render
from django.views.generic import DetailView
from accounts.models import User
from django.shortcuts import redirect
from django.contrib.auth import login, logout
# Create your views here.

class BudgetHome(DetailView):

    def get(self, request):
        template = "budgets/budget_main.html",
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            print(user)

            return render(
                request,
                template,
                {
                    'user': user,
                }
            )
        else:
            return redirect('/accounts/login')
        
class UserLogout(DetailView):
    def get(self, request):
        if request.user:
            logout(request)
        return redirect('/accounts/login')