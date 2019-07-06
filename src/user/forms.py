from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)


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
        '''新規パスワードがoldもしくはbeforeと同じでないか確認

        old_password -- 現在使用中のパスワード
        before_password -- 1つ前に使用していたパスワード
        '''
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password1')
        if old_password == new_password:
            raise forms.ValidationError(
                'The new password is the same as the current password'
            )
        elif self.user.before_password_validator(new_password):
            raise forms.ValidationError(
                'The new password is the same as the previous one'
            )

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


class PasswordAuthForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())


class withdrawalForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())


class UpdateInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text='新しい個人名を入力してください')
    email = forms.EmailField(max_length=254, help_text='新しいメールアドレスを入力してください')

    class Meta():
        model = User
        fields = ('name', 'email')
