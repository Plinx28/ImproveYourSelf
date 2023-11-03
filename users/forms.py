from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, PasswordInput
from django.contrib.auth.models import User
from .models import Person


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Person
        fields = ('email', 'gender', 'first_name', 'last_name', 'birth_date', 'username', 'password1', 'password2', )


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Login')
    password = CharField(label='Password', widget=PasswordInput())

    class Meta:
        model = Person

