# todo/tasks.py

from celery import shared_task
from .models import Todo
from .serializers import TodoSerializer
from django.core.cache import cache
from rest_framework.exceptions import NotFound

CACHE_TIMEOUT = 60 * 15  # 15 minutes

@shared_task
def create_todo_task(data):
    serializer = TodoSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        todo = serializer.save()
        cache.set(f'todo_{todo.slug}', serializer.data, CACHE_TIMEOUT)
    return serializer.data

@shared_task
def get_todos_task():
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    cache.set('todos', serializer.data, CACHE_TIMEOUT)
    return serializer.data

@shared_task
def get_todo_task(slug):
    cached_todo = cache.get(f'todo_{slug}')
    if cached_todo:
        return cached_todo

    try:
        todo = Todo.objects.get(slug=slug)
    except Todo.DoesNotExist:
        raise NotFound('Todo not found')
    
    serializer = TodoSerializer(todo)
    cache.set(f'todo_{slug}', serializer.data, CACHE_TIMEOUT)
    return serializer.data

@shared_task
def update_todo_task(slug, data):
    try:
        todo = Todo.objects.get(slug=slug)
    except Todo.DoesNotExist:
        raise NotFound('Todo not found')
    
    serializer = TodoSerializer(todo, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        todo = serializer.save()
        cache.set(f'todo_{todo.slug}', serializer.data, CACHE_TIMEOUT)
    return serializer.data

@shared_task
def delete_todo_task(slug):
    try:
        todo = Todo.objects.get(slug=slug)
    except Todo.DoesNotExist:
        raise NotFound('Todo not found')
    cache.delete(f'todo_{slug}')
    todo.delete()
