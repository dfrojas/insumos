from django.contrib import admin
from .models import *


class GanadoHembrasAdmin(admin.ModelAdmin):
	list_display = ('predio','tipo_animal','propios','ajenos','totales', )

class GanadoMachosAdmin(admin.ModelAdmin):
	list_display = ('predio','tipo_animal','propios','ajenos','totales', )

admin.site.register(Hembras)
admin.site.register(Machos)
admin.site.register(GanadoHembras,GanadoHembrasAdmin)
admin.site.register(GanadoMachos,GanadoMachosAdmin)
admin.site.register(OtrasEspecies)

admin.site.register(ParametroProductivoDobleProposito)
admin.site.register(ParametroProductivoCeba)
admin.site.register(ParametroProductivoLevante)