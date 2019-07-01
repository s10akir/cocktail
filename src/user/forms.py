from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
                                       PasswordChangeForm)
from django import forms

User = get_user_model()


class SignupForm(UserCreationForm):
    name = forms.CharField(max_length=50, help_text='個人名を入力してください')
    email = forms.EmailField(max_length=254, help_text='メールアドレスを入力してください')

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


class PasswordUpdateForm(PasswordChangeForm):
    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password1')
        if old_password == new_password:
            raise forms.ValidationError("パスワードが同じ")
        else:
            self.save()

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
