from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('fuentes_agua.views',
	url(r'^fuentesagua/nacimientos/.*$', NacimientosAguaView.as_view(),name='nacimientos'),
	url(r'^fuentesagua/usos/.*$', UsosAguaView.as_view(),name='usos'),
	url(r'^update/nacimientos-agua/(?P<predio_id>[-_\w]+)/$', NacimientosAguaUpdateView.as_view(),name='updatenacimientosagua'),
	url(r'^update/usos-agua/(?P<predio_id>[-_\w]+)/$', UsosAguaUpdateView.as_view(),name='updateusossagua'),

	) 




