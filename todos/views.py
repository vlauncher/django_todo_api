from rest_framework import generics
from .models import Todos
from .serializers import TodosSerializer


class TodosView(generics.ListCreateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer


class TodosDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    lookup_field = 'slug'