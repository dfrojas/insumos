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
from .models import *
from predio.models import *
from setup.views import PredioMixin, UpdateModelMixin

class ProduccionLecheView(PredioMixin,CreateView):
	form_class = FormProduccionLeche
	success_url = '/'
	template_name = 'lacteos/produccion_leche.html'

class SuplementosView(PredioMixin,CreateView):
	form_class = FormSuplementos
	success_url = '/'
	template_name = 'lacteos/suplementos.html'

class InsumosView(PredioMixin,CreateView):
	form_class = FormInsumos
	success_url = '/'
	template_name = 'lacteos/insumos.html'

#edit

class ProduccionLecheUpdateView(UpdateModelMixin, UpdateView):
	model = ProduccionLeche
	form_class = FormProduccionLeche
	success_url = '/'
	template_name = 'lacteos/edit/produccion_leche.html'

class SuplementosUpdateView(UpdateModelMixin, UpdateView):
	model = Suplemento
	form_class = FormSuplementos
	success_url = '/'
	template_name = 'lacteos/edit/suplementos.html'

class InsumosUpdateView(UpdateModelMixin, UpdateView):
	model = Insumo
	form_class = FormInsumos
	success_url = '/'
	template_name = 'lacteos/edit/insumos.html'


