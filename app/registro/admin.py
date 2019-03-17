from django.contrib import admin
from .models import *

class AdminSolicitudes(admin.ModelAdmin):
	list_display = [
		"solicitante",
		"numero_de_oficio",
		"remitente",
		"fecha",
		"caso_planteado",
		"tipo_solicitud",
		"adjunto_ci_menor",
		"adjunto_constancia_r",
		"adjunto_ci",
		"adjunto_carnetp",
		"adjunto_gmv",
		"adjunto_casoriesgo",
		"adjunto_informe"
	]

admin.site.register(Solicitudes, AdminSolicitudes)

class AdminCita(admin.ModelAdmin):
	list_display = [
		"solicitud",
		"fecha",
		"hora",
		"trabajador"

	]

admin.site.register(Cita, AdminCita)
admin.site.register(Inspecciones)