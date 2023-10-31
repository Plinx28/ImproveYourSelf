from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, PasswordInput
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = EmailField(max_length=250, label='E-mail')
    first_name = CharField(max_length=250)
    last_name = CharField(max_length=250)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Login')
    password = CharField(label='Password', widget=PasswordInput())

    class Meta:
        model = User

