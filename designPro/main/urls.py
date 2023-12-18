from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/logout', logout_user, name='logout'),
    path('accounts/register', Register.as_view(), name='register'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/profile/', profile, name='profile'),
]