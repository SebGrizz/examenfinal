from django.shortcuts import render
from django.http import response

# Create your views here.

def index (request,*cadena,**cadenaI):
    return render(request, 'pagina/grizzly.html')

def consultoria (request,*cadena,**cadenaI):
    return render(request, 'pagina/consultoria.html')