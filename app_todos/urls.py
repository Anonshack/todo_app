from django.urls import path

from .views import TodoListView, TodosCreateView


urlpatterns = [
    path('list/<int:fk>/', TodoListView.as_view(), name='todo-list'),
    path('new', TodosCreateView.as_view(), name='todo-new'),
]