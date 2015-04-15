from django.contrib import admin
from .models import *

admin.site.register(Persona)
admin.site.register(Rol)
admin.site.register(RelacionPredioPersona)
admin.site.register(Habitantes)

