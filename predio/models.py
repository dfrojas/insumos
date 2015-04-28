from django.db import models
from opciones.models import *
from django.contrib.auth.models import User

class InfoPredioGeneral(models.Model):
	user = models.ForeignKey(User)
	nombre_predio = models.CharField(max_length=30,blank=True,null=True)
	coordenada_n = models.CharField(max_length=20,blank=True,null=True)
	coordenada_w = models.CharField(max_length=20,blank=True,null=True)
	ext_total = models.IntegerField(blank=True,null=True)
	area_arrendamiento = models.IntegerField(blank=True,null=True)
	altitud = models.IntegerField(blank=True,null=True)
	arecipitacion = models.IntegerField(blank=True,null=True)
	km_cabecera_mpal = models.IntegerField(blank=True,null=True)
	acceso_predio_anio = models.CharField(max_length=10,blank=True,null=True)
	medio_transporte_predio = models.CharField(max_length=10,blank=True,null=True)
	tenencia_finca = models.CharField(max_length=3,blank=True,null=True)
	utiliza_sabanas_comunales = models.ForeignKey(Booleanos)
	viven_producido = models.ForeignKey(Booleanos,related_name='viven del producido+')
	total_area_pastoreo = models.IntegerField(blank=True,null=True)
	total_banco_forraje = models.IntegerField(blank=True,null=True)
	total_bosque = models.IntegerField(blank=True,null=True)
	total_cultivo = models.IntegerField(blank=True,null=True)
	total_plantacion_forestal = models.IntegerField(blank=True,null=True)
	total_sistema_agroforestal = models.IntegerField(blank=True,null=True)
	total_uso_suelo = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.nombre_predio


class CreditoPredio(models.Model):

	TIPO_CUOTA = (
		('Mensual','Mensual'),
		('Semestral','Semestral'),
	)

	BOOLEANOS = (
		('Si','Si'),
		('No','No'),
	)

	TIPO_INCENTIVO = (
		('ICR','Incentivo a la Capitalizacion Rural'),
		('CIF','Certificado de Incentivo Agroforestal'),
		('TDF','Tasa de Interes'),
		('IAT','Incentivo de Asistencia Tecnica'),
		('EP','Extension Predial'),
		('Otro','Otro'),
	)
	nombre_pestana = models.CharField(max_length=100)
	predio = models.ForeignKey(InfoPredioGeneral)
	cantidad_predio = models.CharField(max_length=10,blank=True,null=True)
	origen_credito = models.CharField(max_length=100,blank=True,null=True)
	lugar_expedicion = models.CharField(max_length=100,blank=True,null=True)
	pago_cuota = models.IntegerField(blank=True,null=True)
	tipo_cuota = models.CharField(max_length=30,choices=TIPO_CUOTA,blank=True,null=True)
	uso_principal = models.CharField(max_length=100,blank=True,null=True)
	posee_incentivo = models.CharField(max_length=2,choices=BOOLEANOS,blank=True,null=True)
	tipo_incentivo = models.CharField(max_length=100,choices=TIPO_INCENTIVO,blank=True,null=True)
	ingresos_externos = models.CharField(max_length=2,choices=BOOLEANOS,blank=True,null=True)
	posee_subsidio = models.CharField(max_length=2,choices=BOOLEANOS,blank=True,null=True)

	def __str__(self):
		return self.predio.nombre_predio

class ViviendaPredio(models.Model):

	predio = models.ForeignKey(InfoPredioGeneral)
	posee_vivienda = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	cubierta = models.ForeignKey(Cubierta,related_name='cubierta+',blank=True,null=True)
	tipo_construccion = models.ForeignKey(TipoConstruccion,related_name='tipo construccion+',blank=True,null=True)
	estado_saneamiento = models.ForeignKey(BMR,related_name='bueno malo regular+',blank=True,null=True)
	bateria_sanitaria = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	energia_electrica = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	energia_alternativa = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	fuente_energia = models.ForeignKey(FuenteEnergia,related_name='fuente energia+',blank=True,null=True)
	energia_preparacion_alimentos = models.ManyToManyField(FuenteEnergiaPreparacionAlimentos,related_name='fuente energia+',blank=True,null=True)

	def __str__(self):
		return self.predio.nombre_predio
