from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Todos


# Create your views here.
class TodoListView(ListView):
    # model = Todos
    template_name = 'todos/list.html'

    def get_queryset(self):
        try:
            fk = self.kwargs['fk']
            queryset = Todos.objects.filter(user=fk)
        except:
            queryset = Todos.objects.all()
        return queryset


class TodosCreateView(LoginRequiredMixin, CreateView):
    model = Todos
    template_name = 'todos/todos_new.html'
    fields = ('title', 'description', 'start_time', 'end_time', 'status')
    success_url = '/users/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)