from django import forms
from django.forms import DateTimeField
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from .models import Profile, Post, Comment
from captcha.fields import CaptchaField


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите тот же самый пароль еще раз для проверки')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные пароли не совпадают', code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        user.is_activated = True
        if commit:
            user.save()
        return user

    class Meta:
        model = Profile
        fields = (
            'username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'gender', 'birthday',
            'bio',
            'avatar')


class ChangeUserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'bio', 'avatar')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput,
            'post': forms.HiddenInput
        }

