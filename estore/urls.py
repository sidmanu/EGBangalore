from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^locate/', views.locate, name = 'locate'),
	url(r'^contact/', views.contact, name = 'contact'),
]
