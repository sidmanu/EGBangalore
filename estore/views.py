from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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
	return render(request, 'estore/index.html', context)

def locate(request):
	context = {}
	return render(request, 'estore/locate.html', context)

def contact(request):
	context = {}
	return render(request, 'estore/contact.html', context)
