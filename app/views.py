from django.shortcuts import render
from .models import Producto

# Create your views here.

#def es una funcion o metodo 

def home(request):
    productos = Producto.object.all() #hace consulta transofrma datos a una lista de productos
    data = {
        'productos': productos  # 'productos' > esto es el nombre de la variable 
    }
    return render(request, 'app/home.html')


def contacto(request):
    return render(request, 'app/contacto.html')


def galeria(request):
    return render(request, 'app/galeria.html')