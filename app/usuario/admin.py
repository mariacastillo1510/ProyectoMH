from django.contrib import admin
from .models import *

class AdminPUser(admin.ModelAdmin):
	list_display = [
		"id",
		"user",
		"nacionalidad",
		"p_nombre",
		"s_nombre",
		"p_apellido",
		"s_apellido",
		"fecha",
		"genero",
		"telefono",
		"esta_civil",
		"nivel_instruc",
		"profesion",
		"cargo",
		"trabaja",
		"inscrito",
		"registro",
		"pareja",
		"ingre_mensual",
		"direccion"
	]

admin.site.register(PUser, AdminPUser)

