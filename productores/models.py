from django.db import models
from predio.models import *

class Persona(models.Model):
	TIPO_IDENTIFICACION = (
		('CC','Cedula Ciudadania'),
		('NIT','NIT'),
	)
	GENERO = (
		('M','Masculino'),
		('F','Femenino'),
	)

	ESTADO_CIVIL = (
		('Soltero','Soltero'),
		('Casado','Casado'),
		('Union Libre','Union Libre'),
	)
	tipo_identificacion = models.CharField(max_length=5,choices=TIPO_IDENTIFICACION)
	numero_identificacion = models.CharField(max_length=20)
	primer_nombre = models.CharField(max_length=30)
	segundo_nombre = models.CharField(max_length=30)
	primer_apellido = models.CharField(max_length=30)
	segundo_apellido = models. CharField(max_length=30)
	genero = models.CharField(max_length=1,choices=GENERO)
	fecha_nacimiento = models.DateField(max_length=10)
	lugar_nacimiento = models.CharField(max_length=30)
	email = models.EmailField(max_length=50)
	telefono = models.CharField(max_length=15)
	direccion_residencia = models.CharField(max_length=50)
	estad_civil = models.CharField(max_length=50,choices=ESTADO_CIVIL)
	regimen_salud = models.CharField(max_length=30)
	sisben = models.CharField(max_length=10)
	extranjero = models.BooleanField(default=False)

	def __str__(self):
		return self.primer_nombre

class Rol(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre


class RelacionPredioPersona(models.Model):
	predio = models.ForeignKey(Predio)
	persona = models.ForeignKey(Persona,related_name='persona')
	rol = models.ForeignKey(Rol,related_name='rol')

	def __str__(self):
		return self.predio.nombre

class Habitantes(models.Model):
	predio = models.ForeignKey(Predio)
	cantidad_ninos = models.IntegerField()
	cantidad_ninas = models.IntegerField()
	cantidad_adulto_masculino = models.IntegerField()
	cantidad_adulto_femenino = models.IntegerField()
	cantidad_adultos_mayores_masculino = models.IntegerField()
	cantidad_adultos_mayores_femenino = models.IntegerField()
	totalninos = models.IntegerField()
	total_adultos = models.IntegerField()
	total_adultos_mayores = models.IntegerField()

	def __str__(self):
		return self.predio.nombre




