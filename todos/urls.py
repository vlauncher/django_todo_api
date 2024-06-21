from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodosView.as_view()),
    path('<slug:slug>/', views.TodosDetailView.as_view()),
]