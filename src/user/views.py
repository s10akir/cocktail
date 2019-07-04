from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordChangeDoneView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import SignupForm
from .forms import LoginForm
from .forms import PasswordUpdateForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            authenticate(email=email, password=raw_password)
            return redirect('/user/login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def loggedout(request):
    return render(request, 'loggedout.html')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'password-change.html'
    form_class = PasswordUpdateForm
    success_url = reverse_lazy('user:password_change_done')


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'password-change-done.html'
