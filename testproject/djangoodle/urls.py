from django.conf.urls import url, patterns, include
from djangoodle import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$',views.EventDetailView.as_view(), name='event'),	
	)