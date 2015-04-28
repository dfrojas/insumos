from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('manejo_finca.views',
	url(r'^manejo-finca/manejo-general/.*$', ManejoGeneralFincaView.as_view(),name='manejogeneral'),
	url(r'^manejo-finca/enfermedades/.*$', EnfermedadesView.as_view(),name='enfermedadas'),
	url(r'^manejo-finca/practicas-animales/.*$', PracticasAnimalesView.as_view(),name='practicas'),
	url(r'^manejo-finca/vacunas/.*$', VacunasView.as_view(),name='vacunas'),
	#edit
	url(r'^update/manejo-finca/general-y-potreros/(?P<predio_id>\d+)/$', ManejoGeneralUpdateView.as_view()),
	url(r'^update/manejo-finca/enfermedadas/(?P<predio_id>\d+)/$', EnfermedadesUpdateView.as_view()),
	url(r'^update/manejo-finca/practicas-animales/(?P<predio_id>\d+)/$', PracticasAnimalUpdateView.as_view()),
	url(r'^update/manejo-finca/vacunas/(?P<predio_id>\d+)/$', VacunasUpdateView.as_view()),
	) 




