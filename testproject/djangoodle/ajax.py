from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.shortcuts import get_object_or_404, render
from djangoodle.models import Event, Participant
from djangoodle.forms import EventForm, ParticipantForm

@dajaxice_register
def sayhello(request):
    return simplejson.dumps({'message':'Hello World'})

@dajaxice_register
def add_participant(request,event_id):
    e = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        print form
        # if form.is_valid():
        name = form.cleaned_data['name']
        # print "Event_id = " + str(event_id)
        p = Participant(name=name,event=e)
        p.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # return HttpResponseRedirect(reverse('djangoodle:event_detail', args=(p.id,)))
    return simplejson.dumps({'message':'Hello World'})