from django import forms
from .models import *

class SolicitudesForm(forms.ModelForm):
	class Meta:
		model = Solicitudes
		fields = (
			"solicitante",
			"numero_de_oficio",
			"remitente",
			"caso_planteado",
			"tipo_solicitud",
			"adjunto_ci_menor",
			"adjunto_constancia_r",
			"adjunto_ci",
			"adjunto_carnetp",
			"adjunto_gmv",
			"adjunto_casoriesgo",
			"adjunto_informe"
			)

class CitaForm(forms.ModelForm):
	class Meta:
		model = Cita
		fields = (
			'solicitud',
			'fecha',
			'hora', 
			'trabajador'
			)