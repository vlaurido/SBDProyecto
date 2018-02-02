from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.formsets import formset_factory

from facturacionapp.models.generalModels import *
from facturacionapp.forms.generalForms import *

#METODOS DE VERIFICACION
def verificar_empleado(user):
    return user.empleado.rango == "EMPLEADO" or user.empleado.rango == "ADMINISTRADOR"

def verificar_admin(user):
    return user.empleado.rango == "ADMINISTRADOR"

#METODOS DE ACCESO
def login(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            print("ERROR DE AUTENTICACION...")
            return render(request,'login.html', {'error':True})
    else:
        return render(request, 'login.html', {})

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html', {})

def noAccess(request):
    return render(request, 'noAccess.html', {})

@login_required()
def home(request):
    empleado = request.user.empleado
    return render(request, 'home.html', {'empleado': empleado, })

#CRUD CLIENTE

#CREATE
@login_required()
@user_passes_test(verificar_empleado, login_url='noAccess')
def nuevoCliente(request):
    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    elif request.method == "GET":
        form = FormCliente()
        return render(request, 'baseform.html', {'accion': 'Ingreso',
                                                'objeto': 'Cliente',
                                                'form': form,
                                                'empleado': request.user.empleado,})
#READ
@login_required()
@user_passes_test(verificar_empleado, login_url=':noAccess')
def verClientes(request):
    if request.method == "POST":
        ncedula = request.POST["cedula"]
        clientes = Cliente.objects.filter(cedula__contains=ncedula, borrado=False)
        return render(request, 'listClientes.html', {'empleado': request.user.empleado,'clientes': clientes})
    elif request.method == "GET":
        return render(request, 'listClientes.html', {'empleado': request.user.empleado,})
#UPDATE
@login_required()
@user_passes_test(verificar_empleado, login_url='noAccess')
def editarCliente(request, id_cliente):
    cliente = Cliente.objects.get(cedula=id_cliente)
    if request.method == "GET":
        form = FormCliente(instance=cliente)
        return render(request, 'baseform.html', {'accion': 'Edicion', 'objeto': 'Cliente', 'form': form})
    elif request.method == "POST":
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('verClientes')
#DELETE
@login_required()
@user_passes_test(verificar_admin, login_url=':noAccess')
def eliminarCliente(request, id_cliente):
    cliente = Cliente.objects.get(cedula=id_cliente)
    cliente.delete()
    return redirect('verClientes')


#CRUD TOALLA

#CREATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def nuevaToalla(request):
    if request.method == "POST":
        form = FormToalla(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    elif request.method == "GET":
        form = FormToalla()
        return render(request, 'baseform.html', {'empleado': request.user.empleado,'accion': 'Ingreso', 'objeto': 'Toalla', 'form': form})
#READ
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def verToallas(request):
    if request.method == "POST":
        codigo = request.POST["codigo"]
        toallas = Toalla.objects.filter(codigo__contains=codigo, borrado=False)
        return render(request, 'listToallas.html', {'empleado': request.user.empleado,'toallas': toallas})
    elif request.method == "GET":
        return render(request, 'listToallas.html', {'empleado': request.user.empleado,})
#UPDATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def editarToalla(request, id_toalla):
    toalla = Toalla.objects.get(codigo=id_toalla)
    if request.method == "GET":
        form = FormToalla(instance=toalla)
        return render(request, 'baseform.html', {'empleado': request.user.empleado,'accion': 'Edicion', 'objeto': 'Toalla', 'form': form})
    elif request.method == "POST":
        form = FormToalla(request.POST, instance=toalla)
        if form.is_valid():
            form.save()
        return redirect('verToallas')
#DELETE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def eliminarToalla(request, id_toalla):
    toalla = Toalla.objects.get(codigo=id_toalla)
    toalla.delete()
    return redirect('verToallas')

#CRUD ARREGLO

#CREATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def nuevoArreglo(request):
    if request.method == "POST":
        form = FormArreglo(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    elif request.method == "GET":
        form = FormArreglo()
        return render(request, 'baseform.html', {'empleado': request.user.empleado,'accion': 'Ingreso', 'objeto': 'Arreglo', 'form': form})
#READ
@login_required()
@user_passes_test(verificar_empleado, login_url='noAccess')
def verArreglos(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        arreglos = Arreglo.objects.filter(nombre__contains=nombre, borrado=False)
        return render(request, 'listArreglos.html', {'empleado': request.user.empleado,'arreglos': arreglos})
    elif request.method == "GET":
        return render(request, 'listArreglos.html', {'empleado': request.user.empleado,})
#UPDATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def editarArreglo(request, id_arreglo):
    arreglo = Arreglo.objects.get(codigo=id_arreglo)
    if request.method == "GET":
        form = FormArreglo(instance=arreglo)
        return render(request, 'baseform.html', {'empleado': request.user.empleado,'accion': 'Edicion', 'objeto': 'Arreglo', 'form': form})
    elif request.method == "POST":
        form = FormArreglo(request.POST, instance=arreglo)
        if form.is_valid():
            form.save()
        return redirect('verArreglos')
#DELETE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def eliminarArreglo(request, id_arreglo):
    arreglo = Arreglo.objects.get(codigo=id_arreglo)
    arreglo.delete()
    return redirect('verArreglos')


#CRUD INVENTARIO

#CREATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def nuevoInventario(request):
    if request.method == "POST":
        form = FormInventario(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    elif request.method == "GET":
        form = FormInventario()
        return render(request, 'baseform.html', {'empleado': request.user.empleado,'accion': 'Ingreso', 'objeto': 'Registro de inventario', 'form': form})
#READ
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def verInventarios(request):
    inventarios = Inventario.objects.all()
    return render(request, 'listInventario.html', {'empleado': request.user.empleado,'registros': inventarios})
#UPDATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def editarInventario(request, id_registro):
    registro = Inventario.objects.get(id=id_registro)
    if request.method == "GET":
        form = FormInventario(instance=registro)
        return render(request, 'baseform.html', {'accion': 'Edicion',
                                                'objeto': 'Inventario',
                                                'form': form,
                                                'empleado': request.user.empleado,})
    elif request.method == "POST":
        form = FormInventario(request.POST, instance=registro)
        if form.is_valid():
            form.save()
        return redirect('verInventarios')

#NO HAY DELETE INVENTARIO, YA QUE NO ES UNA TRANSACCION OPTIMA

#CRUD FACTURA

#CREATE
@login_required()
@user_passes_test(verificar_empleado, login_url='noAccess')
def nuevaFactura(request):
    formfactura = FormFactura()
    detalle_formset = formset_factory(FormDetalleFactura)
    total = 0
    if request.method == "POST":
        formfactura = FormFactura(request.POST)
        detalle_formset = detalle_formset(request.POST)
        #for detalle_form in detalle_formset:
                #print(detalle_form)
                #arreglo = Arreglo.objects.filter(codigo=detalle_form.cod_arreglo, borrado=False)
                #total += detalle_form.cantidad*arreglo.precio_venta
        if formfactura.is_valid() and detalle_formset.is_valid():
            factura = formfactura.save(commit=False)
            factura.empleado = request.user.empleado
            print(factura)
            factura.save()
            for detalle_form in detalle_formset:
                nuevodetalle = detalle_form.save(commit=False)
                nuevodetalle.cod_factura = factura
                detalle_form.save()
            return redirect('home')
    elif request.method == "GET":
        return render(request, 'formFactura.html', {'formfactura': formfactura,
                                                    'detalle_formset': detalle_formset,
                                                    'empleado': request.user.empleado,
                                                    'total': total })

#CRUD EMPLEADO

#CREATE
@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def nuevoEmpleado(request):
    if request.method == 'POST':
        newUser = FormUser(request.POST)
        newEmployee = FormEmpleado(request.POST)
        if newUser.is_valid() and newEmployee.is_valid():
            user = newUser.save()
            user.set_password(user.password)
            user.save()
            empleado = newEmployee.save(commit=False)
            empleado.usuario = user
            empleado.save()
        return redirect('home')
    else:
        newUser = FormUser()
        newEmployee = FormEmpleado()
    return render(request,'baseform2.html',{'accion': 'Ingreso',
                                            'objeto': 'Empleado',
                                          'form1':newUser,'form2':newEmployee,
                                          'empleado': request.user.empleado,})
#READ
@login_required()
@user_passes_test(verificar_admin, login_url=':noAccess')
def verEmpleados(request):
    if request.method == "POST":
        ncedula = request.POST["cedula"]
        empleados = Empleado.objects.filter(cedula__contains=ncedula, borrado=False)
        return render(request, 'listEmpleados.html', {'empleado': request.user.empleado,'empleados': empleados})
    elif request.method == "GET":
        return render(request, 'listEmpleados.html', {'empleado': request.user.empleado,})

#REPORTES

@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def mas_vendidos(request):
    top_tres = []
    if request.method == 'POST':
        form = FormDateRange(request.POST)
        if form.is_valid():
            top_tres = Arreglo.get_mas_vendidos(form.cleaned_data['startDate'],form.cleaned_data['endDate'])
            return render(request, 'masVendidos.html', {'empleado': request.user.empleado,"top_tres": top_tres, "form":form})
    else:
        form = FormDateRange()
    return render(request, 'masVendidos.html', {'empleado': request.user.empleado,"top_tres": top_tres, "form":form})

@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def best_toallas(request):
    toallas = []
    if request.method == 'POST':
        form = FormDateRange(request.POST)
        if form.is_valid():
            toallas = Toalla.get_mas_demandadas(form.cleaned_data['startDate'],form.cleaned_data['endDate'])
            return render(request, 'toallas.html', {'empleado': request.user.empleado,"toallas": toallas, "form":form})
    else:
        form = FormDateRange()
    return render(request, 'Toallas.html', {'empleado': request.user.empleado,"toallas": toallas, "form":form})


@login_required()
@user_passes_test(verificar_admin, login_url='noAccess')
def ventas(request):
    venta = 0
    if request.method == 'POST':
        form = FormDateRange(request.POST)
        if form.is_valid():
            venta = Factura.get_ventas(form.cleaned_data['startDate'],form.cleaned_data['endDate'])
            return render(request, 'totalVentas.html', {'empleado': request.user.empleado,"venta": venta, "form":form})
    else:
        form = FormDateRange()
    return render(request, 'totalVentas.html', {'empleado': request.user.empleado,"venta": venta, "form":form})
