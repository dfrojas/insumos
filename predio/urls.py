from django.conf.urls import patterns,url
from .views import *
from .models import *
from .forms import *

urlpatterns = patterns('predio.views',
	url(r'^informacionpredio/infogeneral/.*$', InfoGeneralPredioView.as_view(),name='prediogeneral'),
	url(r'^informacionpredio/creditos/.*$', CreditoPredioView.as_view(),name='creditos'),
	url(r'^informacionpredio/vivienda/.*$', ViviendaPredioView.as_view(),name='vivienda'),
	url(r'^update/predio-general/(?P<pk>\d+)/$', UpdatePredioGeneralView.as_view()),
	url(r'^update/predio-credito/(?P<predio_id>\d+)/$', UpdatePredioCreditoView.as_view()),
	url(r'^update/predio-vivienda/(?P<predio_id>\d+)/$', UpdatePredioViviendaView.as_view()),
	) 




