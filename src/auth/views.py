from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView

from .forms import SignupForm
from .forms import LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

class Loggedout(LoginView):
    template_name = 'loggedout.html'
