from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView, DetailView, CreateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from django.shortcuts import get_object_or_404

from .forms import *
from setup.views import UpdateModelMixin

class InfoGeneralPredioView(CreateView):
	form_class = FormInfoGeneralPredio
	success_url = '/'
	template_name = 'predio/infogeneral.html'

	def form_valid(self,form):
		usuario = InfoPredioGeneral()
		usuario = form.save(commit=False)
		usuario.user = self.request.user
		usuario.save()
		return super(InfoGeneralPredioView,self).form_valid(form)

class CreditoPredioView(FormView):
	form_class = FormCreditoPredio
	success_url = '/'
	template_name = 'predio/credito.html'

	def form_valid(self,form):
		creditos = CreditoPredio()
		creditos = form.save(commit=False)
		creditos.predio = InfoPredioGeneral.objects.filter(user_id=self.request.user).latest('id')
		creditos.save()
		return super(CreditoPredioView,self).form_valid(form)

class ViviendaPredioView(CreateView):
	form_class = FormViviendaPreio
	success_url = '/'
	template_name = 'predio/vivienda.html'

	def form_valid(self,form):
		vivienda = ViviendaPredio()
		vivienda = form.save(commit=False)
		vivienda.predio = InfoPredioGeneral.objects.filter(user_id=self.request.user).latest('id')
		vivienda.save()
		return super(ViviendaPredioView,self).form_valid(form)

#EDIT

class UpdatePredioGeneralView(UpdateView):
	model = InfoPredioGeneral
	form_class = FormInfoGeneralPredio
	success_url = '/'
	template_name = 'predio/edit/general.html'

class UpdatePredioCreditoView(UpdateModelMixin,UpdateView):
	model = CreditoPredio
	form_class = FormCreditoPredio
	success_url = '/'
	template_name = 'predio/edit/credito.html'

class UpdatePredioViviendaView(UpdateModelMixin,UpdateView):
	model = ViviendaPredio
	form_class = FormViviendaPreio
	success_url = '/'
	template_name = 'predio/edit/vivienda.html'


