from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	title = models.CharField(max_length=200)
	isbn = models.CharField(max_length=500, unique=True )
	image_url = models.CharField(max_length=100)
	price = models.IntegerField(default=0)

class BookTestimonial(models.Model):
	user = models.ForeignKey(User)
	book = models.ForeignKey(Book)
	text = models.TextField()
	date = models.DateTimeField()

class Stock(models.Model):
	book = models.ForeignKey(Book)
	arrival_date = models.DateTimeField()
	quantity = models.IntegerField()

# Event related

class Event(models.Model):
	title = models.CharField(max_length=200)
	event_short = models.CharField(max_length=300, default='')
	event_detail = models.TextField()
	image_url = models.CharField(max_length=100, default='invalid')
	map_url = models.CharField(max_length=200, default='invalid')
	event_date = models.DateTimeField()
	keywords = models.CharField(max_length=200)
