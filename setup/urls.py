from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('setup.views',
	url(r'^$', LoginView.as_view(),name='login'),
	url(r'^modulos/.*$', Modulos.as_view(),name='modulos'),
	url(r'^edit/.*$', Edit.as_view(),name='edicion'),
	url(r'^reportes/.*$', ListaReportesView.as_view(),name='reportes'),
	url(r'^reporte/(?P<pk>[-_\w]+)/$', ReportesView.as_view(),name='reporte_individual'),
	url(r'^reporte-prueba/.*$', ReportePrueba.as_view()),

	) 




