from django.http import HttpResponse
from django.shortcuts import render
from App_coder.models import Curso

# Create your views here.

def curso(self, nombre,camada):
        #=instancia de ese modelo curso
    curso=Curso(nombre=nombre,camada=camada)
    curso.save()
    return HttpResponse(f"""
    <p>Curso {curso.nombre} - Camada {curso.camada} agregada </p> 
    """)