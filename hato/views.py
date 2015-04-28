from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView, CreateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader

from .forms import *
from opciones.models import *
from predio.models import *
from productores.models import * 
from .models import *
from setup.views import PredioMixin, UpdateModelMixin


class InventarioHembrasView(PredioMixin,CreateView):
	form_class = FormInventarioHembras
	success_url = '/'
	template_name = 'hato/hembras.html'


class InventarioMachosView(PredioMixin,CreateView):
	form_class = FormInventarioMachos
	success_url = '/'
	template_name = 'hato/machos.html'


class OtrasEspeciesView(PredioMixin,CreateView):
	form_class = FormOtrasEspecies
	success_url = '/'
	template_name = 'hato/otras_especies.html'

class DoblePropositoView(PredioMixin,CreateView):
	form_class = FormDobleProposito
	success_url = '/'
	template_name = 'hato/doble_proposito.html'

class CebaView(PredioMixin,CreateView):
	form_class = FormCeba
	success_url = '/'
	template_name = 'hato/ceba.html'

class LevanteView(PredioMixin,CreateView):
	form_class = FormLevante
	success_url = '/'
	template_name = 'hato/levante.html'

#edit
class InventarioHembrasUpdateView(UpdateView):
	model = GanadoHembras
	form_class = FormInventarioHembras
	success_url = '/'
	slug_field = 'tipo_animal'
	slug_url_kwarg = 'tipo_animal'
	template_name = 'hato/edit/inventario_hembras.html'

	def get_object(self):
		print (self.model)
		return get_object_or_404(self.model,predio_id=self.kwargs['predio_id'],predio__user=self.request.user,tipo_animal_id=self.kwargs['tipo_animal'])

class InventarioMachosUpdateView(UpdateView):
	model = GanadoMachos
	form_class = FormInventarioMachos
	slug_field = 'tipo_animal'
	slug_url_kwarg = 'tipo_animal'
	success_url = '/'
	template_name = 'hato/edit/inventario_machos.html'

	def get_object(self):
		print (self.model)
		return get_object_or_404(self.model,predio_id=self.kwargs['predio_id'],predio__user=self.request.user,tipo_animal_id=self.kwargs['tipo_animal'])

class OtrasEspeciesUpdateView(UpdateModelMixin, UpdateView):
	model = OtrasEspecies
	form_class = FormOtrasEspecies
	success_url = '/'
	template_name = 'hato/edit/otras_especies.html'	

class DoblePropositoUpdateView(UpdateModelMixin, UpdateView):
	model = ParametroProductivoDobleProposito
	form_class = FormDobleProposito
	success_url = '/'
	template_name = 'hato/edit/doble_proposito.html'	

class CebaUpdateView(UpdateModelMixin, UpdateView):
	model = ParametroProductivoCeba
	form_class = FormCeba
	success_url = '/'
	template_name = 'hato/edit/ceba.html'	

class LevanteUpdateView(UpdateModelMixin, UpdateView):
	model = ParametroProductivoLevante
	form_class = FormLevante
	success_url = '/'
	template_name = 'hato/edit/levante.html'	
