from django import forms
from django.forms import ModelForm
from .models import *

class FormManejoGeneral(ModelForm):
	class Meta():
		model = ManejoGeneral
		exclude = ("predio",)

class FormEnfermedades(ModelForm):
	class Meta():
		model = EnfermedadesProblemasSanitariosFrecuentes
		exclude = ("predio",)
		
class FormPracticasAnimales(ModelForm):
	class Meta():
		model = LaboresPracticadasAnimal
		exclude = ("predio",)
		
class FormVacunas(ModelForm):
	class Meta():
		model = VacunasAplicadaGanado
		exclude = ("predio",)
		

