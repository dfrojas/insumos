from django.db import models
from predio.models import InfoPredioGeneral
from opciones.models import AtractivoEcoturismo, ActividadEcoturismo


class Agroecoturismo(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	atractivo = models.ManyToManyField(AtractivoEcoturismo)
	actividad = models.ManyToManyField(ActividadEcoturismo)
	observaciones = models.TextField()

	def __str__(self):
		return self.predio.nombre_predio
