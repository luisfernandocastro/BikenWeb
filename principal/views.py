from django.shortcuts import redirect, render
from .models import Persona
from .forms import PersonaForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render (request, 'index.html')

def home(request):
    return render (request, 'pages/inicio.html')

def endReg(request):
    return render (request, 'pages/Message3.html')


def registro(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto={
            'Form':form
        }
    else: 
        form = PersonaForm(request.POST)
        contexto={
            'Form':form
        }
        if form.is_valid():
            form.save()
            messages.success(request,"Inicia sesión para poder continúar")
            return redirect('messagereg')

    return render (request, 'pages/registro.html',contexto)



