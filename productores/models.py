from django.db import models
from predio.models import *
from opciones.models import *

class Persona(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral,related_name='predio+')
	rol = models.ManyToManyField(RolPersona)
	tipo_identificacion = models.ForeignKey(TipoIdentificacion,related_name='tipo identificacion+',blank=True,null=True)
	numero_identificacion = models.CharField(max_length=100,blank=True,null=True)
	primer_nombre = models.CharField(max_length=100)
	segundo_nombre = models.CharField(max_length=100,blank=True,null=True)
	primer_apellido = models.CharField(max_length=100,blank=True,null=True)
	segundo_apellido = models.CharField(max_length=100,blank=True,null=True)
	email = models.EmailField(max_length=100,blank=True,null=True)
	telefono = models.CharField(max_length=100,blank=True,null=True)
	fecha_nacimiento = models.DateField(blank=True,null=True)
	lugar_nacimiento = models.CharField(max_length=100,blank=True,null=True)
	direccion_residencia = models.CharField(max_length=100,blank=True,null=True)
	estado_civil = models.ForeignKey(EstadoCivil,related_name='estado civil+',blank=True,null=True)
	regimen_salud = models.ForeignKey(RegimenSalud,related_name='regimen salud+',blank=True,null=True)
	sisben = models.ForeignKey(Sisben,related_name='sisben+',blank=True,null=True)
	extranjero = models.ForeignKey(Booleanos,related_name='extranjero+',blank=True,null=True)
	genero = models.ForeignKey(Genero,related_name='genero+',blank=True,null=True)

	def __str__(self):
		return self.primer_nombre


class Habitante(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	cantidad_ninos = models.IntegerField()
	cantidad_ninas = models.IntegerField()
	cantidad_adultos_masculino = models.IntegerField()
	cantidad_adultos_femenino = models.IntegerField()
	cantidad_adultos_mayores_masculino = models.IntegerField()
	cantidad_adultos_mayores_femenino = models.IntegerField()
	total_ninos = models.IntegerField(blank=True,null=True)
	total_adultos = models.IntegerField(blank=True,null=True)
	total_adultos_mayores = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.predio.nombre_predio

