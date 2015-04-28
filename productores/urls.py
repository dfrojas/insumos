from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('productores.views',
	url(r'^productor/propietario/.*$', ProductorPropietarioView.as_view(),name='propietario'),
	url(r'^productor/administrador/.*$', ProductorPropietarioAdministradorView.as_view(),name='administrador'),
	url(r'^productor/encargado/.*$', PropietarioAdministradorEncargadoView.as_view(),name='encargado'),
	url(r'^productor/habitantes/.*$', HabitantesView.as_view(),name='habitantes'),
	#URL EDITAR
	url(r'^update/propietario/(?P<predio_id>[-_\w]+)/$', ProductorPropietarioUpdateView.as_view()),
	url(r'^update/administrador/(?P<predio_id>[-_\w]+)/$', ProductorPropietarioAdministradorUpdateView.as_view()),
	url(r'^update/encargado/(?P<predio_id>[-_\w]+)/$', ProductorPropietarioAdministradorEncargadoUpdateView.as_view()),
	url(r'^update/habitantes/(?P<predio_id>[-_\w]+)/$', HabitantesUpdateView.as_view()),
	) 




