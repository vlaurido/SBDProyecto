from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name="login"),
]
