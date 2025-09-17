from django.urls import path
from . import views

urlpatterns = [
    path('<str:alumnos>', views.alumnos, name='alumnos'),
]
