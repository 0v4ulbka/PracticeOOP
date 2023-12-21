from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import logout

from .filters import ApplicationFilter
from .forms import *

from .models import Application


def index(request):
    in_progress = Application.objects.all().filter(status='p').count()
    done = Application.objects.filter(status='d').order_by('-date')

    context = {
        'in_progress': in_progress,
        'done': done
    }

    return render(request, 'main/index.html', context)


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
            return Application.objects.all().order_by('-date')
        else:
            return Application.objects.filter(user=self.request.user).order_by('-date')

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter'] = ApplicationFilter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required
def create_application(request):
    if request.method == 'POST':
        form = AddApplication(request.POST, request.FILES)
        if form.is_valid():
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


class CategoryListView(PermissionRequiredMixin, ListView):
    model = Category
    permission_required = 'user.is_superuser'
    template_name = 'main/category_list.html'


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    model = Category
    form_class = AddCategory
    permission_required = 'user.is_superuser'
    success_url = reverse_lazy('main:category')
    template_name = 'main/category_create.html'


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('main:category')
    else:
        context = {'application': category}
        return render(request, 'main/category_delete.html', context)


# def update_application(request, pk):
#   application = get_object_or_404(Application, pk=pk)
#  if request.method == 'POST':
#     form = ApplicationUpdate(request.POST, request.FILES)
#    if form.is_valid():
#       form.save()
#       return redirect('main:profile')
# else:
#   form = AddApplication()
# return render(request, 'main/application_form.html', {'form': form})

@permission_required('user.is_superuser')
def update_application(request, pk, st):
    newapplication = Application.objects.get(id=pk)
    newapplication.save()

    if st == 'd':
        if request.method == 'POST':
            form = ApplicationUpdateD(request.POST, request.FILES)
            if form.is_valid():
                newapplication.photo_file = form.cleaned_data['photo_file']
                newapplication.status = 'd'
                newapplication.save()
                return redirect('main:profile')
        else:
            form = ApplicationUpdateD()
        return render(request, 'main/application_update.html', {'form': form})

    if st == 'p':
        if request.method == 'POST':
            form = ApplicationUpdateP(request.POST, request.FILES)
            if form.is_valid():
                newapplication.status_comment = form.cleaned_data['status_comment']
                newapplication.status = 'p'
                newapplication.save()
                return redirect('main:profile')
        else:
            form = ApplicationUpdateP()
        return render(request, 'main/application_update.html', {'form': form})
