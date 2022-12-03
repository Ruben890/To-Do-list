from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task


class Home(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'Task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Task"] = context["Task"].filter(user=self.request.user)
        context["count"] = context["Task"].filter(complete=False).count()
        search = self.request.GET.get('search') or ''
        if search:
            context['Task'] = context['Task'].filter(
                title__icontains=search
            )
        context['search'] = search

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'taskDetail.html'
    context_object_name = "Task"


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "taskCreate.html"
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'updateTask.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('Home')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'deleteTask.html'
    context_object_name = 'task'
    success_url = reverse_lazy('Home')


class LoginTask(LoginView):
    template_name = "login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Home')


class register(FormView):
    fields = '__all__'
    template_name = "register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(register, self).form_valid(form)

    def get(self, *args, **kwargs):
         if self.request.user.is_authenticated:
            return redirect('homepage')
         return super(Register, self).get(*args, **kwargs)
