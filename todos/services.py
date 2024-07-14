# todo/services.py

from .tasks import create_todo_task, get_todos_task, get_todo_task, update_todo_task, delete_todo_task
from django.core.cache import cache

def create_todo(data):
    return create_todo_task.delay(data)

def get_todos():
    cached_todos = cache.get('todos')
    if cached_todos:
        return cached_todos  # Return the cached result directly
    return get_todos_task.delay()

def get_todo(slug):
    cached_todo = cache.get(f'todo_{slug}')
    if cached_todo:
        return cached_todo  # Return the cached result directly
    return get_todo_task.delay(slug)

def update_todo(slug, data):
    return update_todo_task.delay(slug, data)

def delete_todo(slug):
    return delete_todo_task.delay(slug)
