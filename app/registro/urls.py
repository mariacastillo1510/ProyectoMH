from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^solicitudes/$', RSolicitudes, name='RSolicitudes'),
	url(r'^citas/$', RCita, name='RCita'),
	url(r'^citas/(?P<pk>[0-9]+)/$', ECita, name="ECita"),
	url(r'^solicitudes/(?P<pk>[0-9]+)/$', ESolicitudes, name="ESolicitudes"),
]