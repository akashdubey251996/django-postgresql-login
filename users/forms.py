from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from users.models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = ('email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    class Meta():
        model = get_user_model()
