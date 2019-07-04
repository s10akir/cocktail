from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('loggedout/', views.loggedout, name='loggedout'),
    path('password-change/',
         views.PasswordChange.as_view(),
         name='password-change'),
    path('password-change-done/',
         views.PasswordChangeDone.as_view(),
         name='password-change-done'),
]
