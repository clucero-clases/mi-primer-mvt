from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    altura = models.FloatField(default=0.0)

class Domicilio(models.Model):
    idPersona = models.BigIntegerField()
    calle = models.CharField(max_length=50)
    numero = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)

class Laboral(models.Model):
    idPersona = models.BigIntegerField()
    actividad = models.CharField(max_length=30)
    antiguedad = models.IntegerField()