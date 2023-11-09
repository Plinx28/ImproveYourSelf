from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, PasswordInput, ModelForm, TextInput, EmailField
from django.contrib.auth.models import User
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'username', 'password1', 'password2')
        

class LoginUserForm(AuthenticationForm):
    username = CharField(label='Login')
    password = CharField(label='Password', widget=PasswordInput())

    class Meta:
        model = User

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
        
