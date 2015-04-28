from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *

class FormPropietario(ModelForm):
	class Meta():
		model = Persona
		exclude = ("predio",)
		
class FormPropietarioAdministrador(ModelForm):
	class Meta():
		model = Persona
		exclude = ("predio",)
		

class FormPropietarioAdministradorEncargado(ModelForm):
	class Meta():
		model = Persona
		exclude = ("predio",)
		
class FormHabitantes(ModelForm):
	class Meta():
		model = Habitante
		exclude = ("predio",'total_ninos','total_adultos','total_adultos_mayores',)
		
