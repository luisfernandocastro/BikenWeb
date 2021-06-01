from django.shortcuts import redirect, render
from .models import *
from .forms import PersonaForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render (request, 'index.html') 

def home(request):
    bicicletas = Bicicletas.objects.all()
    data = {
        'bicicletas' : bicicletas
    }
    return render (request, 'pages/inicio.html',data)

def endReg(request):
    return render (request, 'pages/Message3.html')

def quienesSomos(request):
    return render (request, 'pages/quienessomos.html')


def contacto(request):
    return render (request, 'pages/Contacto.html')


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


def login(request):
    return render (request, 'pages/login.html')


def murouser(request):
    return render (request, 'pages/muroUser.html')



def uploadBike(request):
    return render (request, 'pages/uploadBike.html')