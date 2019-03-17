from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	nacio = (
		("V","V"),
		("E","E"),
	)
	nacionalidad = models.CharField(max_length=50, choices=nacio)
	p_nombre = models.CharField(max_length=40)
	s_nombre = models.CharField(max_length=80, blank=True, null=True)
	p_apellido = models.CharField(max_length=40)
	s_apellido = models.CharField(max_length=80, blank=True, null=True)
	fecha = models.CharField(max_length=10)
	telefono = models.CharField(max_length=40, blank=True, null=True)
	esta_civi = (
		("Casado", "Casado"),
		("Soltero", "Soltero"),
		("Viudo", "Viudo"),
		("Divorciado", "Divorciado"),
	)
	esta_civil = models.CharField(max_length=50, choices=esta_civi)
	nivel = (
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
		("Bachiller", "Bachiller"),
		("Universitario", "Universitario"),
		)
	nivel_instruc = models.CharField(max_length=50, choices=nivel)
	profesion = models.CharField(max_length=50)
	cargos = (
		("Secretaria","Secretaria"),
		("Jefe de Departamento","Jefe de Departamento"),
		("Solicitante","Solicitante"),
	)
	cargo = models.CharField(max_length=50, choices=cargos, default="Solicitante", blank=True, null=True)
	trabaja1 = (
		("Si","Si"),
		("No", "No"),
		)
	trabaja = models.CharField(max_length=50, choices=trabaja1)
	inscrito1 = (
		("Si","Si"),
		("No","No"),
	)
	inscrito = models.CharField(max_length=50, choices=inscrito1)
	posee_registro = (
		("G.M.V.V", "G.M.V.V"),
		("0800 Mi Hogar", "0800 Mi Hogar"),
	)
	registro = models.CharField(max_length=50, choices=posee_registro)
	pare = (
		("Si", "Si"),
		("No", "No"),
	)
	pareja = models.CharField(max_length=20, choices=pare)
	generos = (
		("Femenino","Femenino"),
		("Masculino","Masculino"),
	)
	
	genero = models.CharField(max_length=50, choices=generos)
	ingre_mensual = models.CharField(max_length=20)
	direccion = models.CharField(max_length=500)

	def __str__(self):
		return '%s (%s %s)' %(self.user, self.p_nombre, self.p_apellido)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		PUser.objects.create(user=instance)
	instance.puser.save()