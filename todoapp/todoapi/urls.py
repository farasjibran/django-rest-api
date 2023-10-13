from django.urls import path
from .views import (
  TodoListApiView,
  TodoDetailApiView
)

urlpatterns = [
  path('todos', TodoListApiView.as_view()),
  path('todos/<int:todo_id>', TodoDetailApiView.as_view())
]