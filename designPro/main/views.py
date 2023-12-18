from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth import logout

from .forms import *
from django.contrib import messages

from .models import Application


def index(request):
    return render(request, 'main/index.html')


class Register(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:login')


# class Profile(LoginRequiredMixin, ListView):
# model = User
# template_name = 'main/profile.html'

def profile(request):
    return render(request, 'main/profile.html')


def logout_user(request):
    logout(request)
    return redirect('main:login')
