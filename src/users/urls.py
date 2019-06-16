# users/accounts/urls.py
 
from django.urls import path, include
 
from . import views

from django.contrib.auth import views as auth_views
 
# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'users'
 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
]