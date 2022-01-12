from django.db import models

# Create your models here.

class Familiar(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    relacion = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
