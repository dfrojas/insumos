from django import forms
from django.forms import ModelForm
from .models import *


class FormInventarioHembras(ModelForm):
	class Meta():
		model = GanadoHembras
		exclude = ('predio',)
		
class FormInventarioMachos(ModelForm):
	class Meta():
		model = GanadoMachos
		exclude = ("predio",)
		
class FormOtrasEspecies(ModelForm):
	class Meta():
		model = OtrasEspecies
		exclude = ("predio",)
		

class FormDobleProposito(ModelForm):
	class Meta():
		model = ParametroProductivoDobleProposito
		exclude = ("predio",)
		
class FormCeba(ModelForm):
	class Meta():
		model = ParametroProductivoCeba
		exclude = ("predio",)
		
class FormLevante(ModelForm):
	class Meta():
		model = ParametroProductivoLevante
		exclude = ("predio",)




		