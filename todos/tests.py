from django.test import TestCase
from .models import Todos
import datetime

# Create your tests here.
class TestTodos(TestCase):
    def setUp(self):
        Todos.objects.create(title="test", description="test")

    def test_title(self):
        todo = Todos.objects.get(title="test")
        self.assertEqual(todo.title, "test")

    def test_description(self):
        todo = Todos.objects.get(description="test")
        self.assertEqual(todo.description, "test")

    def test_completed(self):
        todo = Todos.objects.get(completed=False)
        self.assertEqual(todo.completed, False)

    
    
