from django import forms
from django.contrib.auth.models import User
from datetime import date
from facturacionapp.models.generalModels import *

class FormCliente(forms.ModelForm):
    borrado = False
    class Meta:
        model = Cliente
        fields = [
            'cedula',
            'nombre',
            'apellido',
            'direccion',
            'numero_telefonico',
            'correo',
        ]
        labels = {
            'cedula': 'Cédula del cliente*',
            'nombre': 'Nombre del cliente*',
            'apellido': 'Apellido del cliente*',
            'direccion': 'Dirección del cliente*',
            'numero_telefonico': 'Número telefónico*',
            'correo': 'Correo electrónico',
        }
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'id': 'cedula',
                                             'placeholder': 'Cédula del cliente aquí'}),

            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre',
                                             'placeholder': 'Nombre del cliente aquí'}),

            'apellido': forms.TextInput(attrs={'class': 'form-control', 'id': 'apellido',
                                               'placeholder': 'Apellido del cliente aquí'}),

            'direccion': forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion',
                                                'placeholder': 'Dirección del cliente aquí'}),

            'numero_telefonico': forms.TextInput(attrs={'class': 'form-control', 'id': 'numero_telefonico',
                                                        'placeholder': 'Número telefónico del cliente aquí', 'type': 'number'}),

            'correo': forms.TextInput(attrs={'class': 'form-control', 'id': 'correo',
                                             'placeholder': 'Correo electrónico del cliente aquí'})
        }

class FormEmpleado(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = [
            'cedula',
            'nombre',
            'apellido',
            'salario',
            'rango',
        ]
        labels = {
            'cedula': 'Cedula del empleado',
            'nombre': 'Nombre del empleado',
            'apellido': 'Apellido del empleado',
            'salario': 'Salario del empleado',
            'rango': 'Rango del empleado',
        }
        widgets = {
            'cedula' : forms.TextInput(attrs={'class':'form-control','id':'cedula','placeholder':'Cedula del empleado aqui'}),
            'nombre' : forms.TextInput(attrs={'class':'form-control','id':'nombre','placeholder':'Nombre del empleado aqui'}),
            'apellido' : forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'Apellido del empleado aqui'}),
            'salario' : forms.NumberInput(attrs={'class':'form-control','id':'salario','placeholder':'Salario del empleado aqui','min': 366}),
            'rango' : forms.Select(attrs={'class':'form-control','id':'rango','placeholder':'Seleccione rango del empleado'}),
        }

class FormArreglo(forms.ModelForm):
    borrado = False
    class Meta:
        model = Arreglo
        fields = [
            'codigo',
            'nombre',
            'precio_venta',
            'tamanio',
            'canasta',
            'grabado',

        ]
        labels = {
            'codigo': 'Código del arreglo',
            'nombre': 'Nombre del arreglo',
            'precio_venta': 'Precio de venta del arreglo',
            'tamanio': 'Tamaño del arreglo',
            'canasta': 'Lleva canasta',
            'grabado': 'Lleva grabado',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'id': 'codigo', 'placeholder': 'Codigo del arreglo aqui'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre', 'placeholder': 'Nombre del arreglo aqui'}),
            'precio_venta': forms.NumberInput(attrs={'class':'form-control', 'id': 'precio_venta', 'placeholder': 'Precio del arreglo aqui', 'step': 0.01}),
            'tamanio': forms.Select(attrs={'class': 'form-control', 'id': 'tamanio'}),
            'canasta': forms.Select(attrs={'class': 'form-control', 'id': 'canasta'}),
            'grabado': forms.Select(attrs={'class': 'form-control', 'id': 'grabado'}),
        }

class FormToalla(forms.ModelForm):
    borrado = False
    class Meta:
        model = Toalla
        fields = [
            'codigo',
            'color',
            'precio_compra',
            'tamanio',
            'stock',

        ]
        labels = {
            'codigo': 'Código de la toalla',
            'color': 'Color de la toalla',
            'precio_compra': 'Precio de compra de la toalla',
            'tamanio': 'Tamaño de la toalla',
            'stock': 'Stock adquirido',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'id': 'codigo', 'placeholder': 'Codigo de la toalla aqui'}),
            'color': forms.Select(attrs={'class': 'form-control', 'id': 'color'}),
            'precio_compra': forms.NumberInput(attrs={'class':'form-control', 'id': 'precio_compra', 'placeholder': 'Precio de la toalla aqui', 'step': 0.01}),
            'tamanio': forms.Select(attrs={'class': 'form-control', 'id': 'tamanio'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'id': 'stock', 'placeholder': 'Stock de la toalla aqui', 'step': 1}),
        }

class FormFactura(forms.ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget(),initial=date.today,label='Fecha de facturacion')
    class Meta:
        model = Factura
        fields = [
            'codigo',
            'cliente',
            'fecha',
            'tipo_pago'
        ]
        labels = {
            'codigo' : 'Codigo de la factura',
            'cliente' : 'Codigo del cliente',
            'tipo_pago' : 'Tipo de pago'
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control','id':'codigo','placeholder':'Codigo de la factura aqui'}),
            'cliente': forms.TextInput(attrs={'class':'form-control','id':'cliente','placeholder':'Cedula del cliente aqui'}),
            'tipo_pago': forms.Select(attrs={'class':'form-control','id':'tipo_pago'})
        }

class FormDetalleFactura(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = [
            'cod_arreglo',
            'cantidad'
        ]
        labels = {
            'cod_arreglo' : 'Arreglo',
            'cantidad' : 'Cantidad',
        }
        widgets = {
            'cod_arreglo' : forms.Select(),
            'cantidad' : forms.NumberInput(attrs={'min':'1'}),
        }

class FormInventario(forms.ModelForm):
    fecha = forms.DateField(widget=forms.SelectDateWidget(),initial=date.today,label='Fecha de ingreso/salida')
    class Meta:
        model = Inventario
        fields = [
            'cod_toalla',
            'fecha',
            'transaccion',
            'cantidad_toalla',
        ]
        labels = {
            'cod_toalla' : 'Codigo del producto',
            'transaccion' : 'Tipo de transaccion',
            'cantidad_toalla' : 'Cantidad de producto transaccionado',
        }
        widgets = {
            'cod_toalla' : forms.Select(attrs={'class': 'form-control'}),
            'transaccion' : forms.Select(attrs={'class': 'form-control'}),
            'cantidad_toalla' : forms.NumberInput(attrs={'min':1,'class':'form-control','id':'cantidad_toalla','placeholder':'Cantidad de toallas aqui'})
        }

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
        }
        widgets = {
            'username': forms.TextInput
                (attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Su nombre de usuario aqui'}),
            'password': forms.PasswordInput
                (attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Su contraseña aqui'}),
        }
