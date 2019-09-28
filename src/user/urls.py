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
    path('password-authentication/',
         views.passwordAuth,
         name='password-authentication'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('withdrew/', views.withdrew, name='withdrew'),
    path('update-information/', views.updateInfo, name='update-information'),
    path('updated-information/', views.updatedInfo, name='updated-information'),
    path('account/', views.updateInfo, name='account'),
    path('password/', views.PasswordChange.as_view(), name='password'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
]
