from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from djangoodle.models import Event, Participant
from django.views import generic
from datetime import datetime
from django.utils import timezone
from djangoodle.forms import EventForm, ParticipantForm

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

def event_new(request):
	if request.method == 'POST':
		form = EventForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			date = datetime.now()
			p = Event(name=name,description=description,date=date)
			p.save()
			# Always return an HttpResponseRedirect after successfully dealing
			# with POST data. This prevents data from being posted twice if a
			# user hits the Back button.
			return HttpResponseRedirect(reverse('djangoodle:event_detail', args=(p.id,)))
	else:
		form = EventForm()

	return render(request,'djangoodle/event_new.html',{'form':form,}) 

def event_detail(request,event_id):
	participant_form = ParticipantForm()
	e = get_object_or_404(Event, pk=event_id)

# 	if request.method == 'POST':
# 		form = ParticipantForm(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data['name']
			
# 			p = Participant(name=name,event=e)
# 			p.save()
# 			# Always return an HttpResponseRedirect after successfully dealing
# 			# with POST data. This prevents data from being posted twice if a
# 			# user hits the Back button.
# 			# return HttpResponseRedirect(reverse('djangoodle:event_detail', args=(p.id,)))

	return render(request, 'djangoodle/event_detail.html', {
		'event': e,
		'participant_list': e.participant_set.all(),
		'participant_form': participant_form,

	})

# def participant_new(request):
# 	if request.method == 'POST':
# 		form = ParticipantForm(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data['name']
# 			p = Participant(name=name)
# 			p.save()
# 			# Always return an HttpResponseRedirect after successfully dealing
# 			# with POST data. This prevents data from being posted twice if a
# 			# user hits the Back button.
# 			return HttpResponseRedirect(reverse('djangoodle:event_detail', args=(p.id,)))
# 	else:
# 		form = EventForm()

# 	return render(request,'djangoodle/event_new.html',{'form':form,}) 