from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views.generalViews import *


urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^noAccess/$', noAccess, name="noAccess"),

    #URLS DE CRUD CLIENTE
    url(r'^nuevoCliente/$', nuevoCliente, name="nuevoCliente"),
    url(r'^verClientes/$', verClientes, name="verClientes"),
    url(r'^editarCliente/(?P<id_cliente>\w+)/$$', editarCliente, name="editarCliente"),
    url(r'^eliminarCliente/(?P<id_cliente>\w+)/$$', eliminarCliente, name="eliminarCliente"),

    #URLS DE CRUD ARREGLO
    url(r'^nuevoArreglo/$', nuevoArreglo, name="nuevoArreglo"),
    url(r'^verArreglos/$', verArreglos, name="verArreglos"),
    url(r'^editarArreglo/(?P<id_arreglo>\w+)/$$', editarArreglo, name="editarArreglo"),
    url(r'^eliminarArreglo/(?P<id_arreglo>\w+)/$$', eliminarArreglo, name="eliminarArreglo"),

    #URLS DE CRUD TOALLA
    url(r'^nuevaToalla/$', nuevaToalla, name="nuevaToalla"),
    url(r'^verToalla/$', verToallas, name="verToallas"),
    url(r'^editarToalla/(?P<id_toalla>\w+)/$$', editarToalla, name="editarToalla"),
    url(r'^eliminarToalla/(?P<id_toalla>\w+)/$$', eliminarToalla, name="eliminarToalla"),

    #URLS DE CRUD EMPLEADO
    url(r'^nuevoEmpleado/$', nuevoEmpleado, name="nuevoEmpleado"),
]
