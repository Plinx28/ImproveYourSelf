from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import CustomUserCreationForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form: CustomUserCreationForm) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('users:login')
