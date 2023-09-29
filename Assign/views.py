from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (TemplateView,CreateView,DeleteView,UpdateView,ListView,DetailView)
from.import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from.models import task
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User

@method_decorator(login_required, name='dispatch')
class TaskListView(ListView):
    model = task
    template_name = "task.html"
    context_object_name='tasks'

    def get_queryset(self):
        user= self.request.user
        return task.objects.filter(user=user)
class index(TemplateView):
    template_name = "index.html"

@method_decorator(login_required, name='dispatch')
class home(LoginRequiredMixin,CreateView):
    model = task
    template_name = "home.html"
    form_class = forms.CreateTask
    success_url = "/task/"
    def form_valid(self, form):
         user=self.request.user
         form.instance.user = user
         return super().form_valid(form)

class TaskDetailView(DetailView):
    model = task
    template_name = "detail.html"
    context_object_name = 'task'

@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = task
    template_name = "delete.html"
    success_url = reverse_lazy('TaskListView')

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = task
    template_name = "update.html"
    form_class=forms.UpdateForm
    success_url= reverse_lazy('TaskListView')

class Search(TemplateView):
    model = task
    template_name = "search.html"
    def post(self, request):
        query = request.POST.get('query')
        if query:
            user= self.request.user
            results = task.objects.filter(task_name__icontains=query,user=user)
            return render(request, 'search.html', {'tasks': results})
        else:
            return render(request, 'search.html', {'tasks': task.objects.all()})
     
        
     
  


 