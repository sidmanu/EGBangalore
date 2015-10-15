from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=200)
	isbn = models.CharField(max_length=500)
	image_url = models.CharField(max_length=100)
