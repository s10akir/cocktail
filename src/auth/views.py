from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from .forms import SignupForm


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
