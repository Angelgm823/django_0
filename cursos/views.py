from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cursos(request):
    cursosde = [
        {'id':'ingles','descripcion':'esto es un nuevo curso de ingles'},
        {'id': 'frances','descripcion':'esto es un nuevo curso de frances'},
        {'id': 'español','descripcion':'esto es un nuevo curso de español'},
        {'id': 'aleman','descripcion':'esto es un nuevo curso de aleman'},
    ]
    return render(request, 'cursos/cursos.html', {
        'cursosde': cursosde
    })

def cursosNuevos(request, tool):
    return HttpResponse(f'Cursos disponibles: {tool}')
