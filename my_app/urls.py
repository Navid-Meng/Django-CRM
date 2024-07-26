from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path('todos', view=views.todos, name="todos")
]