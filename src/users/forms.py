from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class SignupForm(UserCreationForm):
    name = forms.CharField(label = ('個人名'), max_length = 50, help_text = '個人名を入力してください')
    email = forms.EmailField(label = ('メールアドレス'), max_length = 254, help_text = 'メールアドレスを入力してください')

    # パスワード欄の上書き
    # password1 = forms.CharField(label = ('パスワード'), max_length = 20, widget = forms.PasswordInput(), help_text = 'パスワードを入力してください')
    # password2 = forms.CharField(label = ('パスワード再入力'), max_length = 20, widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')
 