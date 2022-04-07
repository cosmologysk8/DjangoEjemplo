from django.db import models

# Create your models here.
from django.shortcuts import render


class Libro(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    fecha_publicacion = models.DateField()

    # TO STRING de java pero en Puython
    def __str__(self):
        return self.nombre

    # CONSTRUCTOR de java pero en Python
