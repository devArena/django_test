from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from djangoodle.models import Event
from django.views import generic
from django.utils import timezone

class IndexView(generic.ListView):
	template_name = 'djangoodle/index.html'
	context_object_name = 'latest_event_list'

	def get_queryset(self):
		return Event.objects.filter(
		date__lte=timezone.now()
		).order_by('-date')[:5]

class EventDetailView(generic.DetailView):
	template_name = 'djangoodle/event.html'
	model = Event
	
