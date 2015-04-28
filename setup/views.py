from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, FormView, ListView, TemplateView, UpdateView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader

from django.db.models import Sum

from predio.models import *
from productores.models import *
from .forms import *
from hato.models import *

class UpdateModelMixin(object):
	def get_object(self):
		return get_object_or_404(self.model,predio_id=self.kwargs['predio_id'])
	
"""
	def dispatch(self,request,*args,**kwargs):
		p = self.model.objects.filter(predio_id=self.kwargs['predio_id']).count()
		if p==0:
			ctx = {'form':self.form_class}
			return render_to_response('hato/ceba.html',ctx,context_instance=RequestContext(request))
		else:
			return ParametroProductivoDobleProposito.objects.get(predio_id=self.kwargs['predio_id'])
			#return super(UpdateModelMixin,self).dispatch(request,*args,**kwargs)
"""


class PredioMixin(object):
	def form_valid(self,form):
		get_productor = Persona()
		get_productor = form.save(commit=False)
		get_productor.predio = InfoPredioGeneral.objects.filter(user_id=self.request.user).latest('id')
		get_productor.save()
		return super(PredioMixin,self).form_valid(form)

class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'login.html'
	success_url = '/modulos'

	def dispatch(self,request,*args,**kwargs):
		if request.user.is_authenticated():
			return HttpResponseRedirect(self.get_success_url())
		else:
			return super(LoginView,self).dispatch(request,*args,**kwargs)

	def form_valid(self,form):
		login(self.request,form.get_user())
		return super(LoginView,self).form_valid(form)


class Modulos(TemplateView):
	template_name = 'modulos.html'


class Edit(ListView):
	model = InfoPredioGeneral
	template_name = 'edit.html'
	queryset = Persona.objects.all().order_by('?')


class ListaReportesView(ListView):
	model = InfoPredioGeneral
	template_name = 'reportes.html'


class ReportesView(DetailView):
	model = InfoPredioGeneral
	template_name = 'reporte.html'

	def get_context_data(self, **kwargs):
		context = super(ReportesView, self).get_context_data(**kwargs)
		context['propietarios'] = Persona.objects.all()
		#consultas hembras
		context['ganadohembrasvacasparidas'] = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=1)
		context['ganadohembrasvacashorras'] = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=2)
		context['ganadohembras2a3anios'] = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=3)
		context['ganadohembras1a2anios'] = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=4)
		context['ganadohembrasmenores1anio'] = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=5)
		context['ganadohembrasdestete'] = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=6)
		#consultas machos
		context['ganadomachostoros'] = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=1)
		context['ganadomachosmayores3anios'] = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=2)
		context['ganadomachos2a3anios'] = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=3)
		context['ganadomachos1a2anios'] = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=4)
		context['ganadomachosmenores1anio'] = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=5)
		context['ganadomachosbueyes'] = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'],tipo_animal_id=6)
		return context
	


class ReportePrueba(TemplateView):
	template_name = 'reporteprueba.html'






