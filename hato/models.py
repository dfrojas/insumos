from django.db import models
from predio.models import InfoPredioGeneral

class Hembras(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Machos(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre		

class GanadoHembras(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	tipo_animal = models.ForeignKey(Hembras,related_name='animal+',blank=True,null=True)
	propios = models.IntegerField()
	ajenos = models.IntegerField()
	totales = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.predio.nombre_predio
 

class GanadoMachos(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	tipo_animal = models.ForeignKey(Machos,related_name='animal+',blank=True,null=True)	
	propios = models.IntegerField(blank=True,null=True)
	ajenos = models.IntegerField(blank=True,null=True)
	totales = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.predio.nombre_predio

class OtrasEspecies(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	nombre = models.CharField(max_length=100)
	propios = models.IntegerField(blank=True,null=True)
	ajenos = models.IntegerField(blank=True,null=True)
	totales = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.nombre

class ParametroProductivoDobleProposito(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	peso_vaca_produccion = models.IntegerField(blank=True,null=True)
	litro_vaca_dia = models.IntegerField(blank=True,null=True)
	duracion_lactancia = models.IntegerField(blank=True,null=True)
	dias_abiertos = models.IntegerField(blank=True,null=True)
	peso_cria_nacimiento = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.predio.nombre_predio

	class Meta:
		ordering = ('predio',)



class ParametroProductivoCeba(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	peso_inicial_ceba = models.IntegerField()
	edad_ceba = models.IntegerField()
	ganancia_diaria_peso = models.IntegerField()
	tiempo_periodo_ceba = models.IntegerField()
	carga_animal = models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio


class ParametroProductivoLevante(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	peso_destete = models.IntegerField()
	edad_levante = models.IntegerField()
	peso_final_levante = models.IntegerField()
	ganancia_diaria_peso = models.IntegerField()
	tiempo_periodo_levante = models.IntegerField()
	carga_animal = models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio

