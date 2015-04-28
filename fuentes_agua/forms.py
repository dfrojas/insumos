from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *

class FormNacimientosAgua(ModelForm):
	class Meta():
		model = NacimientosAgua
		exclude = ('predio',)

class FormUsosAgua(ModelForm):
	class Meta():
		model = ViviendaUsos
		exclude = ('predio',)


