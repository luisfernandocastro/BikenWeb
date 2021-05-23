from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
# Create your views here.

def index(request):
    return render (request, 'index.html')

def inicio(request):
    return render (request, 'pages/inicio.html')

def registro(request):
    form = PersonaForm()
    contexto={
        'Form':form
    }
    return render (request, 'pages/registro.html',contexto)



