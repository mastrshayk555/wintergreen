from django.shortcuts import render
from django.views.generic import DetailView


class Home(DetailView):
    def get(self, request):
        return render(request, 'site_base/home.html')


class Register(DetailView):
    def get(self, request):
        return render(request, 'site_base/register.html')