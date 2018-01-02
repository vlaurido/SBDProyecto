from django.db import models, connection
from django.contrib.auth.models import User


class Cliente(models.Model):
    #atributos
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.TextField(max_length=50)
    numero_telefonico = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50)

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.nombre,self.apellido)
    def __str__(self):
        return "%s %s" % (self.nombre,self.apellido)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

class Empleado(models.Model):
    #atributos
    cedula = models.CharField(primary_key=True, max_length=10)
    usuario = models.OneToOneField(User, related_name="empleado")
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    salario = models.FloatField()
    rango = models.TextField(max_length=50, choices=(("ADMINISTRADOR", "Administrador"),
                                                     ("EMPLEADO", "Empleado")))

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.nombre,self.apellido)
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

class Arreglo(models.Model):
    #atributos
    nombre = models.CharField(max_length=50)
    precio_venta = models.FloatField()
    tamanio = models.TextField(max_length=50, choices=(('PEQUENIO', 'Pequenino'), ('MEDIANO', 'Mediano'), ('GRANDE', 'Grande')))
    canasta = models.TextField(max_length=50, choices=(('SI', 'Si'), ('NO', 'No')))
    grabado = models.TextField(max_length=50, choices=(('SI', 'Si'), ('NO', 'No')))

    #metodos
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

class Toalla(models.Model):
    #atributos
    codigo = models.CharField(primary_key=True, max_length=20)
    color = models.TextField(max_length=50, choices=(('AMARILLO', 'Amarillo'), ('AZUL', 'Azul'), ('ROJO', 'Rojo'), ('VERDE', 'Verde'),
    ('NARANJA', 'Naranja'), ('MORADO', 'morado'), ('FUCSIA', 'Fucsia'), ('TURQUESA', 'Turquesa')))
    precio_compra = models.FloatField()
    tamanio = models.TextField(max_length=50, choices=(('PEQUENIO', 'Pequenino'), ('MEDIANO', 'Mediano'), ('GRANDE', 'Grande')))
    stock = models.IntegerField()

    #metodos
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

"""
#SIN FORM
class Asignacion(models.Model):
    #relaciones
    toalla = models.ForeignKey(Toalla)
    arreglo = models.ForeignKey(Arreglo)

    #metodos
    def __unicode__(self):
        return self.codigo
    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "Asignacion"
        verbose_name_plural = "Asignaciones"
"""

class Factura(models.Model):
    #relaciones
    cliente = models.ForeignKey(Cliente)
    empleado = models.ForeignKey(Empleado)

    #atributos
    codigo = models.TextField(max_length=10)
    fecha = models.DateField()
    tipo_pago = models.CharField(max_length=20, choices=(('CREDITO', 'Credito'), ('EFECTIVO', 'Efectivo')),
                                 default='EFECTIVO', null=False, blank=False)

    #metodos
    def __unicode__(self):
        return self.codigo
    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

class DetalleFactura(models.Model):
    #relaciones
    cod_factura = models.ForeignKey(Factura)
    cod_producto = models.ForeignKey(Producto)
    #cod_empleado = models.ForeignKey(Empleado)

    #atributos
    cantidad = models.IntegerField()

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.cod_factura,self.cod_producto)
    def __str__(self):
        return "%s %s" % (self.cod_factura,self.cod_producto)

    class Meta:
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Factura"

class Inventario(models.Model):
    #relaciones
    cod_producto = models.ForeignKey(Producto)

    #atributos
    fecha = models.DateField()
    transaccion = models.TextField(max_length=20, choices=(('ENTRADA', 'Entrada'), ('SALIDA', 'Salida')))
    cantidad_producto = models.IntegerField()

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.cod_producto,self.cantidad_producto)
    def __str__(self):
        return "%s %s" % (self.cod_producto,self.cantidad_producto)

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"
