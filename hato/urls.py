from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('hato.views',
	url(r'^hato/hembras/.*$', InventarioHembrasView.as_view(),name='hembras'),
	url(r'^hato/machos/.*$', InventarioMachosView.as_view(),name='machos'),
	url(r'^hato/otras-especies/.*$', OtrasEspeciesView.as_view(),name='otras_especies'),
	url(r'^hato/doble-proposito/.*$', DoblePropositoView.as_view(),name='doble_proposito'),
	url(r'^hato/ceba/.*$', CebaView.as_view(),name='ceba'),
	url(r'^hato/levante/.*$', LevanteView.as_view(),name='ceba'),
	#edit
	url(r'^update/hato/hembras/(?P<predio_id>[-_\w]+)/(?P<tipo_animal>[-_\w]+)/$', InventarioHembrasUpdateView.as_view()),
	url(r'^update/hato/machos/(?P<predio_id>[-_\w]+)/(?P<tipo_animal>[-_\w]+)/$', InventarioMachosUpdateView.as_view()),
	url(r'^update/hato/otras-especies/(?P<predio_id>\d+)/$', OtrasEspeciesUpdateView.as_view()),
	url(r'^update/hato/doble-proposito/(?P<predio_id>\d+)/$', DoblePropositoUpdateView.as_view()),
	url(r'^update/hato/ceba/(?P<predio_id>\d+)/$', CebaUpdateView.as_view()),
	url(r'^update/hato/levante/(?P<predio_id>\d+)/$', LevanteUpdateView.as_view()),

	) 




