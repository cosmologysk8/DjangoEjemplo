from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def mostrar_inicio (request):

    lista_libro = Libro.objects.all() # HACE UNA CONSULTA Y DEVUELVE TODOS LOS LIBROS DE LA BBDD

    return render(request, 'libreria/inicio.html', {'Libros': lista_libro}) # SE LE PASA EN FORMATO JSON

def crear_libro ( request):

    # GET -> DEVOLVER AL USUARIO EL HTML VACÍO
    if request.method == 'GET':
        return render(request, 'libreria/crear_libro.html')
    # POST -> CREAR EL LIBRO EN LA BBDD Y DEVOLVERNOS A LA PANTALLA DE INICIO
    else:
        libro_nuevo = Libro()
        libro_nuevo.id = request.POST.get('id')
        libro_nuevo.nombre = request.POST.get('nombre')
        libro_nuevo.fecha_publicacion = request.POST.get('fecha')
        Libro.save(libro_nuevo)
        return redirect('')