from django import forms
from django.forms import ModelForm
from .models import *
from .views import *

class FormInfoGeneralPredio(ModelForm):
	class Meta():
		model = InfoPredioGeneral
		exclude = ('user','total_area_pastoreo','total_banco_forraje','total_bosque','total_cultivo','total_plantacion_forestal','total_sistema_agroforestal','total_uso_suelo',)
		

class FormCreditoPredio(ModelForm):
	class Meta():
		model = CreditoPredio
		exclude = ('predio',)
		

class FormViviendaPreio(ModelForm):
	class Meta():
		model = ViviendaPredio
		exclude = ('predio',)
	
"""
class PredioGeneralEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PredioGeneralEditForm, self).__init__(*args, **kwargs)
		#for field_name, field in self.fields.items():
		#	field.widget.attrs['class'] = 'form-control' ' width=50px'
	class Meta:
		model = InfoPredioGeneral
		exclude = ('user',)

class PredioCreditoEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PredioCreditoEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = CreditoPredio
		exclude = ('predio',)

class PredioViviendaEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PredioViviendaEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = ViviendaPredio
		exclude = ('predio',)
"""

