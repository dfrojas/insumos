from django import forms
from django.forms import ModelForm
from .models import *

class FormProduccionLeche(ModelForm):
	class Meta():
		model = ProduccionLeche
		exclude = ('predio',)
		
class FormSuplementos(ModelForm):
	class Meta():
		model = Suplemento
		exclude = ('predio',)
		
class FormInsumos(ModelForm):
	class Meta():
		model = Insumo
		exclude = ('predio',)

		