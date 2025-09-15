from django.urls import path
from . import views

urlpatterns = [
    path('<str:clase>', views.clases, name='clases'),
]
