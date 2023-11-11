from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.db import transaction
from django.views.generic import CreateView, DetailView
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from .forms import CustomUserCreationForm, LoginUserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


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

class ProfileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

    def get_context_data(self, *args, **kwargs: Any):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('users:update_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })