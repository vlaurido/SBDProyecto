from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms.formsets import formset_factory

from .models.generalModels import *
from .forms.generalForms import *

def verificar_empleado(user):
    return user.empleado.rango == "EMPLEADO" or user.empleado.rango == "ADMINISTRADOR"

def verificar_admin(user):
    return user.empleado.rango == "ADMINISTRADOR"

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

# Create your views here.
@login_required()
def home(request):
    empleado = request.user.empleado
    return render(request, 'home.html', {'empleado': empleado, })

@login_required()
@user_passes_test(verificar_empleado, login_url='facturacionapp:noAccess')
def nuevoCliente(request):
    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mainapp:home')
    elif request.method == "GET":
        form = FormCliente()
        return render(request, 'baseform.html', {'accion': 'Ingreso',
                                                'objeto': 'Cliente',
                                                'form': form,
                                                'empleado': request.user.empleado,})

@login_required()
@user_passes_test(verificar_admin, login_url='mainapp:noAccess')
def verClientes(request):
    if request.method == "POST":
        ncedula = request.POST["cedula"]
        clientes = Cliente.objects.filter(cedula__contains=ncedula)
        return render(request, 'listClientes.html', {'empleado': request.user.empleado,'clientes': clientes})
    elif request.method == "GET":
        return render(request, 'listClientes.html', {'empleado': request.user.empleado,})

@login_required()
@user_passes_test(verificar_empleado, login_url='mainapp:noAccess')
def editarCliente(request, id_cliente):
    cliente = Cliente.objects.get(cedula=id_cliente)
    if request.method == "GET":
        form = FormCliente(instance=cliente)
        return render(request, 'baseform.html', {'accion': 'Edicion', 'objeto': 'Cliente', 'form': form})
    elif request.method == "POST":
        form = FormCliente(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('mainapp:verClientes')
