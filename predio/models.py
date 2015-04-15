from django.db import models

class Predio(models.Model):
	nombre_predio = models.CharField(max_length=30)
	coordenada_n = models.CharField(max_length=20)
	coordenada_w = models.CharField(max_length=20)
	ext_total = models.IntegerField()
	area_arrendamiento = models.IntegerField()
	altitud = models.IntegerField()
	arecipitacion = models.IntegerField()
	km_abecera_mpal = models.IntegerField()
	acceso_predio_anio = models.CharField(max_length=10)
	medio_transporte_predio = models.CharField(max_length=10)
	tenencia_finca = models.CharField(max_length=3)
	utiliza_sabanas_comunales = models.CharField(max_length=2)
	viven_producido = models.CharField(max_length=2)
	total_area_pastoreo = models.IntegerField()
	total_banco_forraje = models.IntegerField()
	total_bosque = models.IntegerField()
	total_cultivo = models.IntegerField()
	total_plantacion_forestal = models.IntegerField()
	total_sistema_agroforestal = models.IntegerField()
	total_uso_suelo = models.IntegerField()

	def __str__(self):
		return self.nombre_predio