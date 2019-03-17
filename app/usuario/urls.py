from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^registrar/$',RegPUser , name="RegPUser"),
	url(r'^login/$', Login.as_view(), name="Login"),
	url(r'^editar/contraseña/$', EditarClave, name="EditarClave"),
	url(r'^editar/perfil/$', EditarPerfil, name="EditarPerfil"),
	url(r'^asignar/cargo/(?P<pk>[0-9]+)/$', EditarAsignarCargo, name="EditarAsignarCargo"),
	url(r'^logout/$', LogoutView.as_view(), name="Logout"),
]

