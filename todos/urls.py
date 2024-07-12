from .views import TodoViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todos')

urlpatterns = [
    path('', include(router.urls)),
]