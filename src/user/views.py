from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import SignupForm
from .forms import LoginForm
from .forms import PasswordAuthForm


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


@login_required     # ログインしていないと見れないように
def passwordAuth(request):
    if request.method == 'POST':
        form = PasswordAuthForm(request.POST)
        if form.is_valid():
            email = request.user
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                return redirect('/')
            else:
                form.add_error(None, 'パスワードが違います')
    else:
        form = PasswordAuthForm()

    return render(request, 'password-auth.html', {'form': form})
