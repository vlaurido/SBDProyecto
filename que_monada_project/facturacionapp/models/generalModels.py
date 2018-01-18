from django.db import models, connection
from django.contrib.auth.models import User



class Cliente(models.Model):
    #atributos
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.TextField(max_length=50)
    numero_telefonico = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50, null=True, blank=True)
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.nombre,self.apellido)
    def __str__(self):
        return "%s %s" % (self.nombre,self.apellido)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()

class Empleado(models.Model):
    #relaciones
    usuario = models.OneToOneField(User, related_name="empleado", on_delete=models.CASCADE)

    #atributos
    cedula = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    salario = models.FloatField()
    rango = models.CharField(max_length=50, choices=(("ADMINISTRADOR", "Administrador"),
                                                     ("EMPLEADO", "Empleado")))
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.nombre,self.apellido)
    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()

class Arreglo(models.Model):
    #atributos
    codigo = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=50)
    precio_venta = models.FloatField()
    tamanio = models.CharField(max_length=50, choices=(('PEQUEÑO', 'Pequeño'), ('MEDIANO', 'Mediano'), ('GRANDE', 'Grande')))
    canasta = models.CharField(max_length=50, choices=(('SI', 'Si'), ('NO', 'No')))
    grabado = models.CharField(max_length=50, choices=(('SI', 'Si'), ('NO', 'No')))
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Arreglo"
        verbose_name_plural = "Arreglos"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()

class Toalla(models.Model):
    #atributos
    codigo = models.CharField(primary_key=True, max_length=20)
    color = models.TextField(max_length=50, choices=(('AMARILLO', 'Amarillo'), ('AZUL', 'Azul'), ('ROJO', 'Rojo'), ('VERDE OSCURO', 'Verde oscuro'), ('VERDE CLARO', 'Verde claro'),
    ('NARANJA', 'Naranja'), ('MORADO', 'morado'), ('FUCSIA', 'Fucsia'), ('TURQUESA', 'Turquesa')))
    precio_compra = models.FloatField()
    tamanio = models.TextField(max_length=50, choices=(('PEQUENIO', 'Pequeño'), ('MEDIANO', 'Mediano'), ('GRANDE', 'Grande')))
    stock = models.IntegerField()
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Toalla"
        verbose_name_plural = "Toallas"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()

class Factura(models.Model):
    #relaciones
    cliente = models.ForeignKey(Cliente,  on_delete=models.DO_NOTHING)
    empleado = models.ForeignKey(Empleado,  on_delete=models.DO_NOTHING)

    #atributos
    codigo = models.TextField(max_length=10)
    fecha = models.DateField()
    tipo_pago = models.CharField(max_length=20, choices=(('CREDITO', 'Credito'), ('EFECTIVO', 'Efectivo')),
                                 default='EFECTIVO', null=False, blank=False)
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return self.codigo
    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()

class DetalleFactura(models.Model):
    #relaciones
    cod_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cod_arreglo = models.ForeignKey(Arreglo, on_delete=models.DO_NOTHING)
    #cod_empleado = models.ForeignKey(Empleado)

    #atributos
    cantidad = models.IntegerField()
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.cod_factura,self.cod_producto)
    def __str__(self):
        return "%s %s" % (self.cod_factura,self.cod_producto)

    class Meta:
        verbose_name = "Detalle de Factura"
        verbose_name_plural = "Detalles de Factura"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()

class Inventario(models.Model):
    #relaciones
    cod_toalla = models.ForeignKey(Toalla,  on_delete=models.DO_NOTHING)

    #atributos
    fecha = models.DateField()
    transaccion = models.TextField(max_length=20, choices=(('ENTRADA', 'Entrada'), ('SALIDA', 'Salida')))
    cantidad_toalla = models.IntegerField()
    borrado = models.BooleanField(default=False)

    #metodos
    def __unicode__(self):
        return "%s %s" % (self.cod_producto,self.cantidad_producto)
    def __str__(self):
        return "%s %s" % (self.cod_producto,self.cantidad_producto)

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

    def delete(self):
        if not self.borrado:
            self.borrado = True
            self.save()
