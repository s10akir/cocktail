from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .forms import SignupForm
from .forms import LoginForm
from .forms import PasswordAuthForm
from .forms import withdrawalForm
from .forms import UpdateInfoForm


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


@login_required
def withdrawal(request):
    if request.method == 'POST':
        form = withdrawalForm(request.POST)
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
                user.is_active = False
                user.save()
                return redirect('/user/withdrew')
            else:
                form.add_error(None, 'パスワードが違います')
    else:
        form = withdrawalForm()

    return render(request, 'withdrawal.html', {'form': form})


def withdrew(request):
    return render(request, 'withdrew.html')


def updateInfo(request):
    if request.method == 'POST':
        form = UpdateInfoForm(request.POST, instance=request.user)
        email = request.user.email
        if form.is_valid():
            new_email = form.cleaned_data.get('email')
            if email == new_email:
                form.add_error(None, '同じEmailです。別のEmailを入力してください。')
            else:
                form.save()
                return redirect('/user/updated-information')
    elif request.method == 'GET':
        form = UpdateInfoForm(instance=request.user)
    return render(request, 'update-information.html', {'form': form})


def updatedInfo(request):
    return render(request, 'updated-information.html')
