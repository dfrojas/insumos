from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *

class FormPastoreo(ModelForm):
	class Meta():
		model = Pastoreo
		exclude = ('predio',)
		
class FormBancosForraje(ModelForm):
	class Meta():
		model = BancosForraje
		exclude = ('predio',)
		
		
class FormCultivosAgricolas(ModelForm):
	class Meta():
		model = CultivoAgricola
		exclude = ('predio',)
		

class FormCultivosAgricolas(ModelForm):
	class Meta():
		model = CultivoAgricola
		exclude = ('predio',)
				
class FormPlantacionForestales(ModelForm):
	class Meta():
		model = PlantacionForestal
		exclude = ('predio',)

class FormBosquesAreasConservacion(ModelForm):
	class Meta():
		model = BosquesAreasConservacion
		exclude = ('predio',)

		
#edit

class PastoreoEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PastoreoEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Pastoreo
		exclude = ('predio',)

class BancosForrajeEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BancosForrajeEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = BancosForraje
		exclude = ('predio',)

class CultivoAgricolaEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CultivoAgricolaEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = CultivoAgricola
		exclude = ('predio',)




