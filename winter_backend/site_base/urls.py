from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    #path('about', views.About.as_view(), name='about'),
    #path('register', views.Register.as_view(), name='register'),
    #path('contact', views.Contact.as_view(), name='contact'),
    #path('projects', views.Projects.as_view(), name='projects'),
    #path('components', views.components.as_view(), name='components')
]