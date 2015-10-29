from estore.models import Event
from django.utils import timezone

def get_upcoming_events():
	events = Event.objects.filter(event_date__gt=timezone.now())
	return events

def get_event_by_id(eid):
	return Event.objects.get(id=eid)
