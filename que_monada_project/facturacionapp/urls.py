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

    url(r'^nuevoCliente/$', nuevoCliente, name="nuevoCliente"),
    url(r'^verClientes/$', verClientes, name="verClientes"),
    url(r'^editarCliente/(?P<id_cliente>\w+)/$$', editarCliente, name="editarCliente"),
    url(r'^eliminarCliente/(?P<id_cliente>\w+)/$$', eliminarCliente, name="eliminarCliente"),

    url(r'^nuevoArreglo/$', nuevoArreglo, name="nuevoArreglo"),
    url(r'^verArreglos/$', verArreglos, name="verArreglos"),
    url(r'^editarArreglo/(?P<id_arreglo>\w+)/$$', editarArreglo, name="editarArreglo"),
    url(r'^eliminarArreglo/(?P<id_arreglo>\w+)/$$', eliminarArreglo, name="eliminarArreglo"),
]
