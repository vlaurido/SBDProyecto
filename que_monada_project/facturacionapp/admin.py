from django.contrib import admin
from .models.generalModels import *

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Arreglo)
admin.site.register(Factura)
admin.site.register(DetalleFactura)
admin.site.register(Toalla)
admin.site.register(Inventario)
