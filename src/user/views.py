from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView

from .forms import SignupForm
from .forms import LoginForm
from .forms import UpdateForm


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


def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=request.user)
        email = request.user.email
        if form.is_valid():
            new_email = form.cleaned_data.get('email')
            if email == new_email:
                form.add_error(None, '同じEmailです。別のEmailを入力してください。')
            else:
                form.save()
                return redirect('/user/updated-information')
    elif request.method == 'GET':
        form = UpdateForm(instance=request.user)
    return render(request, 'update-information.html', {'form': form})


def updated(request):
    return render(request, 'updated-information.html')
