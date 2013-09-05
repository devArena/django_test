from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from djangoodle.models import Event
from django.views import generic
from django.utils import timezone
from djangoodle.forms import EventForm

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

def event(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			# TODO store event to database
			return HttpResponseRedirect(reverse('djangoodle:index'))
	else:
		form = EventForm()

	return render(request,'djangoodle/event2.html',{'form':form,}) 