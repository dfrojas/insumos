from django.db import models
from predio.models import InfoPredioGeneral
from opciones.models import Booleanos


class EnfoqueDiferencial(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	es_victima = models.ForeignKey(Booleanos,related_name='es victima+')
	observaciones = models.TextField()

	def __str__(self):
		return self.predio.nombre_predio