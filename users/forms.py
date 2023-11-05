from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, EmailField, PasswordInput, ChoiceField, DateField
from django.contrib.auth.models import User
from .utils import MyDateInput, GENDER_CHOICES


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(max_length=250, label='E-mail')
    gender = ChoiceField(choices=GENDER_CHOICES)
    birth_date = DateField(label='Birthday', widget=MyDateInput())
    
    class Meta:
        model = User
        fields = ('email', 'gender', 'first_name', 'last_name', 'birth_date', 'username', 'password1', 'password2')
        # widgets = {
        #     'email': EmailField(max_length=250, label='E-mail'),
        #     'gender': ChoiceField(choices=GENDER_CHOICES),
        #     'birth_date': DateField(label='Birthday', widget=MyDateInput())
        # }


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Login')
    password = CharField(label='Password', widget=PasswordInput())

    class Meta:
        model = User

