from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
                                       PasswordChangeForm)

from django import forms

from user.models.user import User


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
    # 新規パスワードがoldもしくはbeforeを同じでないか確認
    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password1')
        if old_password == new_password:
            raise forms.ValidationError('パスワードが同じ')
        elif self.user.old_password_validator(new_password):
            raise forms.ValidationError('前回のパスワードと同じ')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        self.user.set_before_password(self.cleaned_data['old_password'])
        if commit:
            self.user.save()
        return self.user
