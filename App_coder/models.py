from django.db import models
from django.forms import ModelChoiceField

# Create your models here.
#un modelo es una clase 
class Curso(models.Model):#la clase curso hereda de la clase models.Model
    #estructura de la base de datos
    nombre = models.CharField( max_length=40)#mchar #columna
    camada = models.IntegerField()#mint

class Estudiante(models.Model):
    
    nombre = models.CharField( max_length=30)
    apellido = models.CharField( max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    
    nombre = models.CharField( max_length=30)
    apellido = models.CharField( max_length=30)
    email = models.EmailField()
    profesion= models.CharField( max_length=30)

class Entregable(models.Model):
    
    nombre = models.CharField( max_length=30)
    fechaDeEntrega= models.DateField()
    entregado=models.BooleanField()

