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

class PastoreoView(PredioMixin,CreateView):
	form_class = FormPastoreo
	success_url = '/'
	template_name = 'usos_suelo/pastoreo.html'

class BancosForrajeView(PredioMixin,CreateView):
	form_class = FormBancosForraje
	success_url = '/'
	template_name = 'usos_suelo/bancosforraje.html'

class CultivosAgricolasView(PredioMixin, CreateView):
	form_class = FormCultivosAgricolas
	success_url = '/'
	template_name = 'usos_suelo/cultivos_agricolas.html'

class PlantacionForestalesView(PredioMixin, CreateView):
	form_class = FormPlantacionForestales
	success_url = '/'
	template_name = 'usos_suelo/cultivos_agroforestales.html'

#edit

class PastoreoUpdateView(UpdateModelMixin, UpdateView):
	model = Pastoreo
	form_class = FormPastoreo
	success_url = '/'
	template_name = 'usos_suelo/edit/pastoreo.html'

class BancosForrajeUpdateView(UpdateModelMixin, UpdateView):
	model = BancosForraje
	form_class = FormBancosForraje
	success_url = '/'
	template_name = 'usos_suelo/edit/bancos_forraje.html'

class CultivoAgricolaUpdateView(UpdateModelMixin, UpdateView):
	model = CultivoAgricola
	form_class = FormCultivosAgricolas
	success_url = '/'
	template_name = 'usos_suelo/edit/cultivos_agricolas.html'

class CultivoAgroForestalUpdateView(UpdateModelMixin, UpdateView):
	model = PlantacionForestal
	form_class = FormPlantacionForestales
	success_url = '/'
	template_name = 'usos_suelo/edit/cultivos_agroforestales.html'

class BosquesAreasConservacionUpdateView(UpdateModelMixin, UpdateView):
	model = BosquesAreasConservacion
	form_class = FormBosquesAreasConservacion
	success_url = '/'
	template_name = 'usos_suelo/edit/bosques_conservacion.html'
