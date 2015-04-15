from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import DetailView, CreateView, FormView, ListView, TemplateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required


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