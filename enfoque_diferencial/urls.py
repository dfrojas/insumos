from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('enfoque_diferencial.views',
	url(r'^enfoque_diferencial/.*$', EnfoqueDiferencialView.as_view(),name='enfoque_diferencial'),
	#edit
	url(r'^update/enfoque_diferencial/(?P<predio_id>\d+)/$', EnfoqueDiferencialUpdateView.as_view()),
	) 




