from django.contrib import admin
from .models import Marca, Producto
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "descripcion", "nuevo","marca", "fecha_fabricacion" ]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["nuevo", "marca"]
    list_per_page = 4





admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)