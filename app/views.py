from django.shortcuts import render
from .models import Producto
from .forms import ContactoForm

# Create your views here.

#def es una funcion o metodo 

def home(request):
    productos = Producto.objects.all() #hace consulta transforma datos a una lista de productos
    data = {
        'productos': productos  # 'productos' > esto es el nombre de la variable 
    }
    return render(request, 'app/home.html', data)


def contacto(request):
    data = {
        'form': ContactoForm() # 'form' es el nombre de la variable
    }

    if  request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario


    return render(request, 'app/contacto.html', data)


def galeria(request):
    return render(request, 'app/galeria.html')