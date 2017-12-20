from django.contrib import admin
from .models.role import *
from .models.profile import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Role)
