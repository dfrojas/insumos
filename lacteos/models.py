from django.db import models
from predio.models import InfoPredioGeneral


class Comprador(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class TipoSuplemento(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class TipoInsumo(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre


class ProduccionLeche(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	total_producido_litro_dia = models.IntegerField()
	cantidad_destinada_productos_lacteos = models.IntegerField()
	cantidad_destinada_autoconsumo_dia = models.IntegerField()
	precio_litro_leche = models.IntegerField()
	promedio_vacas_ordenadas_dia = models.IntegerField()
	mantequilla = models.IntegerField()
	yogurth = models.IntegerField()
	kumis = models.IntegerField()
	dulces = models.IntegerField()
	queso_de_mano = models.IntegerField()
	queso_cuajada = models.IntegerField()
	queso_prensado = models.IntegerField()
	queso_maduro = models.IntegerField()
	a_quien_vende = models.ManyToManyField(Comprador)

	def __str__(self):
		return self.predio.nombre_predio

class Suplemento(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	suplemento =  models.ForeignKey(TipoSuplemento,related_name='suplemento+')
	cantidad = models.IntegerField()
	valor_unitario = models.IntegerField()
	valor_total = models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio

class Insumo(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	insumo =  models.ForeignKey(TipoInsumo,related_name='insumos+')
	cantidad = models.IntegerField()
	valor_unitario = models.IntegerField()
	valor_total = models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio




