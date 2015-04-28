from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('usos_suelo.views',
	url(r'^usossuelo/pastoreo/.*$', PastoreoView.as_view(),name='pastoreo'),
	url(r'^usossuelo/bancos-forraje/.*$', BancosForrajeView.as_view(),name='bancosforraje'),
	url(r'^usossuelo/cultivos-agricolas/.*$', CultivosAgricolasView.as_view(),name='cultivos'),
	url(r'^usossuelo/cultivos-agroforestales/.*$', PlantacionForestalesView.as_view(),name='cultivos'),
	#edit
	url(r'^update/pastoreo/(?P<predio_id>\d+)/$', PastoreoUpdateView.as_view()),
	url(r'^update/bancos-forraje/(?P<predio_id>\d+)/$', BancosForrajeUpdateView.as_view()),
	url(r'^update/cultivos-agricolas/(?P<predio_id>\d+)/$', CultivoAgricolaUpdateView.as_view()),
	url(r'^update/cultivos-agroforestales/(?P<predio_id>\d+)/$', CultivoAgroForestalUpdateView.as_view()),

	) 




