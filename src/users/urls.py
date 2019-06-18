# users/accounts/urls.py
 
from django.urls import path, include
 
from . import views

from django.contrib.auth import views as auth_views
 
# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'users'
 
urlpatterns = [
    path('login/', views.Login.as_view(), name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
