from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class SignupForm(UserCreationForm):
    name = forms.CharField(max_length = 50, help_text = '個人名を入力してください')
    email = forms.EmailField(max_length = 254, help_text = 'メールアドレスを入力してください')

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')
 