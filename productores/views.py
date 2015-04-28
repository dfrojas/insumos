from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from .forms import *
from opciones.models import *
from setup.views import UpdateModelMixin, PredioMixin

class ProductorPropietarioView(PredioMixin,FormView):
	form_class = FormPropietario
	success_url = '/'
	template_name = 'productores/propietario.html'


class ProductorPropietarioAdministradorView(PredioMixin,FormView):
	form_class = FormPropietarioAdministrador
	success_url = '/'
	template_name = 'productores/administrador.html'

class PropietarioAdministradorEncargadoView(PredioMixin,FormView):
	form_class = FormPropietarioAdministradorEncargado
	success_url = '/'
	template_name = 'productores/encargado.html'

class HabitantesView(PredioMixin,FormView):
	form_class = FormHabitantes
	success_url = '/'
	template_name = 'productores/habitantes.html'

#EDIT

class  ProductorPropietarioUpdateView(UpdateModelMixin,UpdateView):
	model = Persona
	form_class = FormPropietario
	success_url = '/'
	template_name = 'productores/edit/propietario.html'

class  ProductorPropietarioAdministradorUpdateView(UpdateModelMixin,UpdateView):
	model = Persona
	form_class = FormPropietarioAdministrador
	success_url = '/'
	template_name = 'productores/edit/administrador.html'

class  ProductorPropietarioAdministradorEncargadoUpdateView(UpdateModelMixin,UpdateView):
	model = Persona
	form_class = FormPropietarioAdministradorEncargado
	success_url = '/'
	template_name = 'productores/edit/encargado.html'

class HabitantesUpdateView(UpdateModelMixin,UpdateView):
	model = Habitante
	form_class = FormHabitantes
	success_url = '/'
	template_name = 'productores/edit/habitantes.html'

