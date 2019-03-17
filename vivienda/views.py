from django.shortcuts import render
from app.registro.models import *
from app.usuario.models import *

def Inicio(request):
	if request.user.is_active:
		solicitantes = PUser.objects.values('cargo').filter(cargo="Solicitante")
		return render(request, "panel.html", {"solicitantes":solicitantes})
		
	else:
		return render(request, "index.html", {})