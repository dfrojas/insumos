from django.db import models
from predio.models import *
from opciones.models import *

class NacimientosAgua(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	cantidad_corrientes = models.IntegerField()
	protege_corrientes = models.ForeignKey(Booleanos,related_name='booleanos+')
	cantidad_zonas_rurales = models.IntegerField()
	forma_proteccion = models.ForeignKey(FormaProteccion,related_name='forma proteccion agua+')

	def __str__(self):
		return self.predio.nombre_predio

class ViviendaUsos(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	agua_uso_domestico = models.ManyToManyField(AguaUsoDomestico)
	agua_produccion = models.ManyToManyField(AguaProduccion)
	sistema_succion_agua = models.ManyToManyField(SistemaSuccionAgua)

	def __str__(self):
		return self.predio.nombre_predio




