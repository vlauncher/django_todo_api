# todo/urls.py

from django.urls import path
from .views import TodoListCreateView, TodoDetailView

urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<slug:slug>/', TodoDetailView.as_view(), name='todo-detail'),
]
