from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('lacteos.views',
	url(r'^lacteos/produccion-leche/.*$', ProduccionLecheView.as_view(),name='produccionleche'),
	url(r'^lacteos/suplementos/.*$', SuplementosView.as_view(),name='suplementos'),
	url(r'^lacteos/insumos/.*$', InsumosView.as_view(),name='insumos'),
	#edit
	url(r'^update/lacteos/produccion-leche/(?P<predio_id>\d+)/$', ProduccionLecheUpdateView.as_view()),
	url(r'^update/lacteos/suplementos/(?P<predio_id>\d+)/$', SuplementosUpdateView.as_view()),
	url(r'^update/lacteos/insumos/(?P<predio_id>\d+)/$', InsumosUpdateView.as_view()),

	) 




