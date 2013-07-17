from django.db import models
import datetime
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField('event date')

    def __unicode__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=30)
    event = models.ForeignKey('Event')

    time_items = models.ManyToManyField('TimeItem')

    def __unicode__(self):
        return self.name

class TimeItem(models.Model):
    event = models.ForeignKey('Event')
    time_start = models.DateTimeField('suggested start time')

