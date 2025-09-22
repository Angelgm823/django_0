from django.urls import path
from . import views

urlpatterns = [
    path('home', views.cursos, name='cursos'),
    path('cursos/<str:tool>', views.cursosNuevos, name='cursosde')
]