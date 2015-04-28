from django.db import models
from predio.models import *
from opciones.models import *


class ManejoGeneral(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	sistema_reproduccion = models.ForeignKey(SistemaReproduccion,related_name='sistema de reproduccion+')
	realiza_chequeo = models.ForeignKey(Booleanos,related_name='booelanos+')
	cria_ternerno_macho = models.ForeignKey(Booleanos,related_name='booelanos+')
	edad_cria = models.IntegerField()

	def __str__(self):
		return self.predio.nombre_predio

class Enfermadades(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class EnfermedadesProblemasSanitariosFrecuentes(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	enfermedad = models.ManyToManyField(Enfermadades)

	def __str__(self):
		return self.predio.nombre_predio


class LaboresAnimal(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Vacunas(models.Model):
	nombre = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class LaboresPracticadasAnimal(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	labor_practicada_a_animal = models.ManyToManyField(LaboresAnimal)

	def __str__(self):
		return self.predio.nombre_predio

class VacunasAplicadaGanado(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	vacuna = models.ManyToManyField(Vacunas)

	def __str__(self):
		return self.predio.nombre_predio


