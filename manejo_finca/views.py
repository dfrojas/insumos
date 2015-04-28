from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import BaseFormView
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from .forms import *
from opciones.models import *
from predio.models import *
from productores.models import * 
from setup.views import PredioMixin, UpdateModelMixin

class ManejoGeneralFincaView(PredioMixin,CreateView):
	form_class = FormManejoGeneral
	success_url = '/'
	template_name = 'manejo_finca/manejo_general.html'

class EnfermedadesView(PredioMixin,CreateView):
	form_class = FormEnfermedades
	success_url = '/'
	template_name = 'manejo_finca/enfermedades.html'

class PracticasAnimalesView(PredioMixin,CreateView):
	form_class = FormPracticasAnimales
	success_url = '/'
	template_name = 'manejo_finca/practica_animales.html'

class VacunasView(PredioMixin,CreateView):
	form_class = FormVacunas
	success_url = '/'
	template_name = 'manejo_finca/vacunas.html'

#edit

class ManejoGeneralUpdateView(UpdateModelMixin, UpdateView):
	model = ManejoGeneral
	form_class = FormManejoGeneral
	success_url = '/'
	template_name = 'manejo_finca/edit/manejo_general.html'

class EnfermedadesUpdateView(UpdateModelMixin, UpdateView):
	model = EnfermedadesProblemasSanitariosFrecuentes
	form_class = FormEnfermedades
	success_url = '/'
	template_name = 'manejo_finca/edit/enfermedades.html'

class PracticasAnimalUpdateView(UpdateModelMixin, UpdateView):
	model = LaboresAnimal
	form_class = FormPracticasAnimales
	success_url = '/'
	template_name = 'manejo_finca/edit/practica_animales.html'

class VacunasUpdateView(UpdateModelMixin, UpdateView):
	model = Vacunas
	form_class = FormVacunas
	success_url = '/'
	template_name = 'manejo_finca/edit/vacunas.html'



