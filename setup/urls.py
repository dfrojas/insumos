from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('setup.views',
	url(r'^$', LoginView.as_view(),name='login'),
	url(r'^modulos/.*$', Modulos.as_view(),name='modulos'),
	
	) 




