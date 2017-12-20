from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views.generalViews import *


urlpatterns = [
    #URLS DE INCIO/CIERRE/PERMISOS
    url(r'^$', home, name="home"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
]
