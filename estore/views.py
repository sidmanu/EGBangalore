from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import estore.queries as queries

def login_user(request):
	context = {}
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')
	return render(request, 'estore/login.html', context)

@login_required(login_url='/login/')
def index(request):
	context = {}
	events = queries.get_upcoming_events()	
	context['events'] = events
	return render(request, 'estore/index.html', context)

def locate(request):
	context = {}
	return render(request, 'estore/locate.html', context)

def contact(request):
	context = {}
	return render(request, 'estore/contact.html', context)

def faq(request):
	context = {}
	return render(request, 'estore/faq.html', context)

def event(request, event_id):
	context = {}
	event = queries.get_event_by_id(event_id)
	context['event'] = event
	return render(request, 'estore/event_more.html', context)

def events(request):
	context = {}
	events = queries.get_upcoming_events()	
	context['events'] = events
	return render(request, 'estore/events.html', context)

def about_us(request):
	context = {}
	return render(request, 'estore/about_us.html', context)
