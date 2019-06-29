from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView

from .forms import SignupForm
from .forms import LoginForm
from .forms import withdrawalForm


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


def withdrawal(request):
    if request.method == 'POST':
        form = withdrawalForm(request.POST)
        if form.is_valid():
            email = request.user
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                user.is_active = False
                user.save()
                return redirect("/")    
    else:
        form = withdrawalForm()

    return render(request, 'withdrawal.html', {'form': form})
