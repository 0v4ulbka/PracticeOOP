from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth import logout

from .forms import *

from .models import Application


def index(request):
    return render(request, 'main/index.html')


class Register(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:login')


def logout_user(request):
    logout(request)
    return redirect('main:login')


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'main/application_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Application.objects.all()
        else:
            return Application.objects.filter(user=self.request.user)


@login_required
def create_application(request):
    if request.method == 'POST':
        form = AddApplication(request.POST, request.FILES)
        if form.is_valid():
            # try:
            #   Application.objects.create(**form.cleaned_data)
            #   return redirect('main:profile')
            # except:
            #   form.add_error(None, 'Ошибка добавления заявки')
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('main:profile')
    else:
        form = AddApplication()
    return render(request, 'main/application_form.html', {'form': form})


@login_required
def application_delete(request, pk):
    application = get_object_or_404(Application, pk=pk)
    if not request.user.is_author(application):
        return redirect('main:profile')
    if request.method == 'POST':
        application.delete()
        return redirect('main:profile')
    else:
        context = {'application': application}
        return render(request, 'main/application_delete.html', context)

