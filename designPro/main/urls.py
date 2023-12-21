from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('accounts/logout', logout_user, name='logout'),
    path('accounts/register', Register.as_view(), name='register'),
    path('accounts/login', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('accounts/profile/', ApplicationListView.as_view(), name='profile'),
    path('application/create', create_application, name='application_create'),
    path('application/delete/<int:pk>', application_delete, name='application_delete'),
    path('application/update/<int:pk><str:st>', update_application, name='status_update'),
    path('category', CategoryListView.as_view(), name='category'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('category/delete/<int:pk>', category_delete, name='category_delete')
]

