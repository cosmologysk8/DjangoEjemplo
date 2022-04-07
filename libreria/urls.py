
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',mostrar_inicio),
    path('libros/crear', crear_libro)
    #path('Lirbos',),

]
