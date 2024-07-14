# todo/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from . import services

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        result = services.get_todos()
        if isinstance(result, dict):  # If it's a cached result
            todos = result
        else:
            todos = result  # Wait for the async result
        return Response(todos, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        result = services.create_todo(request.data)
        todo = result.get(timeout=10)  # Wait for the async result
        return Response(todo, status=status.HTTP_201_CREATED)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        result = services.get_todo(kwargs['slug'])
        if isinstance(result, dict):  # If it's a cached result
            todo = result
        else:
            todo = result  # Wait for the async result
        return Response(todo, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        result = services.update_todo(kwargs['slug'], request.data)
        todo = result  # Wait for the async result
        return Response(todo, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        result = services.delete_todo(kwargs['slug'])
        result.get(timeout=10)  # Wait for the async result
        return Response(status=status.HTTP_204_NO_CONTENT)
