from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = {}
	return render(request, 'estore/index.html', context)

def locate(request):
	context = {}
	return render(request, 'estore/locate.html', context)

def contact(request):
	context = {}
	return render(request, 'estore/contact.html', context)
