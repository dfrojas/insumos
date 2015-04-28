from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *

class FormAgroecoturismo(ModelForm):
	class Meta():
		model = Agroecoturismo
		exclude = ("predio",)
