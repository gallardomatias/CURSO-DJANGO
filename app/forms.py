from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensajes", "avisos"]
        fields = '__all__' # sirve para importar todo con el orden que tiene el modelo sin mas, el de arriba uno elige
        