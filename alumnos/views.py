from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

# Create your views here.


clase = {
    'inglés': 'Clase de Inglés',
    'Frances': 'Clase de Frances',
    'Español': 'Clase de Español'
}


def clases_day(request, clase):
    clases = list(clase.keys())
    if clase > len(clases):
        return HttpResponse('Clase no existe')
    redirect_clase = clases[clase]
    return HttpResponseRedirect(f'/alumnos/clase{redirect_clase}')

def clases(request, clase):

    try:
        alumno_text = clase[clase]
        return HttpResponse(alumno_text)
    except:
        return HttpResponseNotFound('No existe esta clase')
