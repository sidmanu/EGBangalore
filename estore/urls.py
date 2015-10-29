from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^locate/', views.locate, name = 'locate'),
	url(r'^faq/', views.faq, name = 'faq'),
	url(r'^events/', views.events, name = 'events'),
	url(r'^event/(?P<event_id>\d+)/$', views.event, name = 'event_more'),
	url(r'^contact/', views.contact, name = 'contact'),
	url(r'^about-us/', views.about_us, name = 'about_us'),
]
