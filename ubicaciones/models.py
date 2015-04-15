from django.db import models
from predio.models import *

class Pais(models.Model):
	nombre = models.CharField(max_length=100)
	codigo_pais = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Departamento(models.Model):
	pais = models.ForeignKey(Pais)
	nombre = models.CharField(max_length=100)
	codigo_departamento = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Municipio(models.Model):
	departamento = models.ForeignKey(Departamento)
	nombre = models.CharField(max_length=100)
	codigo_municipio = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Corregimiento(models.Model):
	municipio = models.ForeignKey(Municipio)
	nombre = models.CharField(max_length=100)
	codigo_corregimiento = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Vereda(models.Model):
	corregimiento = models.ForeignKey(Corregimiento)
	predio  = models.ForeignKey(Predio,related_name='predio')
	nombre = models.CharField(max_length=100)
	codigo_vereda = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

		