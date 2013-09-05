from django import forms

class EventForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    date = forms.DateTimeField()
