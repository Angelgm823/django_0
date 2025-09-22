from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    stack = [
        {'id': 'python', 'name': 'python3'},
        {'id': 'Angular', 'name': 'Angular v20'},
        {'id': 'c++', 'name': 'c++'},
        {'id': 'javascript', 'name': 'js'},
    ]
    return render(request, "landing/landing.html", {
        'nombre': 'Angel',
        'edad': 25,
        'fecha': datetime.today(),
        'stack': stack
    })


def stack_detail(request, tool):
    return HttpResponse(f'tecnologia: {tool}')