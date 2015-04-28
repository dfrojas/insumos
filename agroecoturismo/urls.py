from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('agroecoturismo.views',
	url(r'^agroecoturismo/.*$', AgroecoturismoView.as_view(),name='agroecoturismo'),
	#edit
	url(r'^update/agroecoturismo/(?P<predio_id>\d+)/$', AgroecoturismoUpdateView.as_view()),

	) 




