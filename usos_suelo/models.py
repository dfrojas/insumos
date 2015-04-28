from django.db import models
from predio.models import *
from opciones.models import *

class Pastoreo(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral,related_name='predio')
	pasturas_nativas_sin_arboles = models.IntegerField()
	pasturas_introducidas_sin_arboles = models.IntegerField()
	arboles_dispersos_en_potreros = models.IntegerField()
	franjas_dobles_arboles_en_potreros = models.IntegerField()
	cercas_vivas = models.IntegerField()
	sistema_silvopastoril_intensivo = models.IntegerField()
	sistema_silvopastoril_intensivo_con_maderables = models.IntegerField()


	def __str__(self):
		return self.predio.nombre_predio


class BancosForraje(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral,related_name='nombre del predio+')
	bancos_energia = models.IntegerField()
	bancos_proteina = models.IntegerField()
	bancos_mixtos = models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio


class CultivoAgricola(models.Model):
	tipo = models.ForeignKey(TipoSiembra)
	predio = models.ForeignKey(InfoPredioGeneral)
	nombre = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	area_cultivada = models.IntegerField()
	area_cosechada = models.IntegerField()
	anio_establecimiento = models.CharField(max_length=20)
	rendimiento = models.CharField(max_length=20)

	def __str__(self):
		return self.predio.nombre_predio

class PlantacionForestal(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	tipo = models.ForeignKey(TipoSiembra)
	nombre_plantacion = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=100)
	area_cultivada = models.IntegerField()
	area_cosechada = models.IntegerField()
	anio_establecimiento = models.CharField(max_length=20)
	rendimiento = models.CharField(max_length=20)

	def __str__(self):
		return self.predio.nombre_predio

class BosquesAreasConservacion(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	area_regeneracion_natural = models.IntegerField()
	area_cultivada = models.IntegerField()
	matas_monte = models.IntegerField()
	morichal = models.IntegerField()
	estereo = models.IntegerField()
	raudal= models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio





