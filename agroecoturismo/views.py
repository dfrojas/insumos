from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView, CreateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from .forms import *
from opciones.models import *
from productores.models import Persona
from setup.views import PredioMixin, UpdateModelMixin

class AgroecoturismoView(PredioMixin, CreateView):
	form_class = FormAgroecoturismo
	success_url = '/'
	template_name = 'agroecoturismo/index.html'

class AgroecoturismoUpdateView(UpdateModelMixin, UpdateView):
	model = Agroecoturismo
	form_class = FormAgroecoturismo
	success_url = '/'
	template_name = 'agroecoturismo/edit/index.html'