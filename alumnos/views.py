from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404

# Create your views here.


clases = {
    "ingles": 'Clase de Inglés',
    "hola": "esto es una nueva prueba",
    "frances": 'Clase de Francés',
    "español": 'Clase de Español'
}


def clases_dayNew(request, claseNew):
    days = list(clases.keys())
    # Convertir claseNew a entero si viene como string
    try:
        clase_index = int(claseNew)
    except (ValueError, TypeError):
        return HttpResponse('Índice de clase inválido')

    # Verificar que el índice esté dentro del rango válido
    if clase_index < 0 or clase_index >= len(days):
        return HttpResponse('Clase no existe')

    redirect_clase = days[clase_index]
    return HttpResponseRedirect(f'/alumnos/{redirect_clase}/')


def alumnos(request, alumnos):  # Cambia claseNew por alumnos
    try:
        alumno_text = clases[alumnos]
        return HttpResponse(f'<h1>{alumno_text}</h1>')
    except KeyError:
        #return HttpResponseNotFound('<h1>No existe esta clase</h1>')
        return render(request, '404.html')
        #raise Http404() # Cuando esta en producción