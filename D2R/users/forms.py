from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField

from D2R.users.models import Profile

UserModel = get_user_model()


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
                'autofocus': True,
                'class': 'input',
                }))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={
                'autocomplete': 'current-password',
                'class': 'input',
                }))

    error_messages = {
        'invalid_login': (
            "Please enter a correct %(username)s and password."
        ),
        'inactive': "This account is inactive.",
    }


class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'The two password fields didn’t match.',
    }
    password1 = forms.CharField(
        label="Password",
        strip=False,
        help_text="",
        widget=forms.PasswordInput(attrs={'class': 'input'}),
    )
    password2 = forms.CharField(
        label="Confirm your password",
        strip=False,
        help_text="",
        widget=forms.PasswordInput(attrs={'class': 'input'}),
    )

    class Meta:
        model = UserModel
        fields = ("email",)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'input', 'required': 'required'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)
