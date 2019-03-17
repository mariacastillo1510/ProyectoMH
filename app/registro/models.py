from __future__ import unicode_literals
from django.db import models
from app.usuario.models import *

class Solicitudes(models.Model):
	solicitante = models.ForeignKey(PUser)
	numero_de_oficio = models.IntegerField(null=True, blank=True)
	oficina = (
		('Departamentos de Redes Populares','Departamentos de Redes Populares'),
			)
	remitente = models.CharField(max_length=200,choices=oficina, null=True, blank=True)
	fecha = models.DateField(auto_now_add=True)
	caso_planteado = models.CharField(max_length=1000)
	tipo = (
		('Personal','Personal'),
		('Alto Riezgo','Alto Riezgo'),
		('Salud','Salud'),
		('Institucional','Institucional')
		)
	tipo_solicitud = models.CharField(max_length=200,choices=tipo, null=True, blank=True)


	adjunto_ci_menor = models.ImageField(upload_to="adjuntado")
	adjunto_constancia_r = models.ImageField(upload_to="adjuntado")
	adjunto_ci = models.ImageField(upload_to="adjuntado")
	adjunto_carnetp = models.ImageField(upload_to="adjuntado")
	adjunto_gmv = models.ImageField(upload_to="adjuntado")
	adjunto_casoriesgo = models.ImageField(upload_to="adjuntado", null=True, blank=True)
	adjunto_informe= models.ImageField(upload_to="adjuntado", null=True, blank=True)
	def __str__(self):
		return '%s - %s' % (self.numero_de_oficio,self.solicitante)

class Cita(models.Model):
	solicitud = models.OneToOneField(Solicitudes)
	fecha = models.CharField(max_length=10)
	hora = models.CharField(max_length=10)
	trabajador = models.ForeignKey(PUser)

	def __str__(self):
		return '%s' %(self.solicitud)

class Inspecciones(models.Model):
	cita = models.OneToOneField(Cita)
	municipios = (
		('Guanare ','Guanare'),
		('Agua Blanca','Agua Blanca'),
		('Araure','Araure'),
		('Esteller','Esteller'),
		('Guanarito','Guanarito'),
		('Monseñor Jose Vicente de Unda','Monseñor Jose Vicente de Unda'),
		('Ospino','Ospino'),
		('Paez','Paez'),
		('Papelon','Papelon'),
		('San Genaro de Boconoito','San Genaro de Boconoito'),
		('San Rafael de Onoto','San Rafael de Onoto'),
		('Santa Rosalia','Santa Rosalia'),
		('Sucre','Sucre'),
		('Turen','Turen')
		)
	municipios = models.CharField(max_length=200,choices=municipios, null=True, blank=True)
	gre = (
		("Córdoba","Córdoba"),
		("Guanare","Guanare"),
		("San José de la Montaña","San José de la Montaña"),
		("San Juan de Guanaguanare","San Juan de Guanaguanare"),
		("Virgen de Coromoto","Virgen de Coromoto"),
	)
	grep = models.CharField(max_length=100, choices=gre, null=True, blank=True)

	aguablanca =(
		("Agua Blanca","Agua Blanca"),
	)
	aguablancap = models.CharField(max_length=100, choices=aguablanca, null=True, blank=True)

	araure =(
		("Rio Acarigua","Rio Acarigua"),
		("araure","araure"),
	)
	araurep = models.CharField(max_length=100, choices=araure, null=True, blank=True)

	esteller =(
		("Piritu","Piritu"),
		("Uveral","Uveral"),
	)
	estellerp = models.CharField(max_length=100, choices=esteller, null=True, blank=True)

	guanarito =(
		("Guanarito","Guanarito"),
		("Divina Pastora","Divina Pastora"),
		("Trinidad de la Capilla","Trinidad de la Capilla"),
	)
	guanaritop = models.CharField(max_length=100, choices=guanarito, null=True, blank=True)

	josevicentedeunda =(
		("Peña Blanca","Agua Blanca"),
	)
	josevicentedeundap = models.CharField(max_length=100, choices=josevicentedeunda, null=True, blank=True)

	ospino =(
		("Aparicio","Aparicio"),
		("Estacion","Estacion"),
		("Ospino","Ospino"),
	)
	ospinop = models.CharField(max_length=100, choices=ospino, null=True, blank=True)

	paez =(
		("Aramendi","Aramendi"),
 		("Amparo","Amparo"),
 		("Camilo","Camilo"),
 		("Urbana Guasdualito","Urbana Guasdualito"),
 		("Urdaneta","Urdaneta"),
	)
	paezp = models.CharField(max_length=100, choices=paez, null=True, blank=True)

	papelon = (
		("Caño Delgadito","Caño Delgadito"),
		("San Rafael Apóstol de Papelón","San Rafael Apóstol de Papelón"),
	)
	papelonp = models.CharField(max_length=100, choices=papelon, null=True, blank=True)


	sangenaro = (
		("Antolín Tovar Anquino","Antolín Tovar Anquino"),
		("Boconoíto","Boconoíto"),
	)
	sangenarop = models.CharField(max_length=100, choices=sangenaro, null=True, blank=True)

	sanrafaeldeonoto = (
		("Santa Fé","Santa Fé"),
 		("San Rafael de Onoto","San Rafael de Onoto"),
		("Thermo Morales","Thermo Morales"),
	)
	sanrafaeldeonotop = models.CharField(max_length=100, choices=sanrafaeldeonoto, null=True, blank=True)

	santarosalia = (
		("Santa Rosalia","Santa Rosalia"),
 		("Florida","Florida"),
		
	)
	santarosaliap = models.CharField(max_length=100, choices=santarosalia, null=True, blank=True)

	sucre= (
		("Sucre","Sucre"),
		("Concepción","Concepción"),
 		("San José de Saguaz","San José de Saguaz"),
 		("San Rafael de Palo Alzado","San Rafael de Palo Alzado"),
 		("Uvencio Antonio Velásquez","Uvencio Antonio Velásquez"),
 		("Villa Rosa","Villa Rosa"),
	)
	sucrep = models.CharField(max_length=100, choices=sucre, null=True, blank=True)

	turen = (
		("Canelones","Canelones"),
 		("Capital Turén","Capital Turén"),
 		("Santa Cruz","Santa Cruz"),
	)
	turenp = models.CharField(max_length=100, choices=turen, null=True, blank=True)

	tlf_habitacion = models.CharField(max_length=12)

	descr_vivienda = (
		("Casa","Casa"),
 		("Rural","Rural"),
 		("Rancho","Rancho"),
 		("Apartamento","Apartamento"),
 		("Quinta","Quinta"),
 		("Barraca","Barranca"),
 		("Tabla","Tabla"),
 		
	)
	descr_viviendap = models.CharField(max_length=100, choices=descr_vivienda, null=True, blank=True)

	tipo_pared = (
		("Frisada","Frisada"),
 		("Sin Frisada","Sin Frisada"),
 		("Adobe","Adobe"),
 		("Zinc","Zinc"),
 		("Tabla","Tabla"),
 		("Carton","Carton"),
 		("Carton Piedra","Carton Piedra"),
 		
	)
	tipo_paredp = models.CharField(max_length=100, choices=tipo_pared, null=True, blank=True)

	tipo_piso = (
		("Cemento","Cemento"),
 		("Rustico","Rustico"),
 		("Tierra","Tierra"),
 		("Balbosa","Balbosa"),
 		("granito","granito"),
 		("Cemento Pulido","Cemento Pulido"),
 		
	)
	tipo_pisop = models.CharField(max_length=100, choices=tipo_piso, null=True, blank=True)

	tipo_techo = (
		("Aceroli","Aceroli"),
 		("Zinc","Zinc"),
 		("Platabanda","Platabanda"),
 		("Tejas","Tejas"),
 		("Raso","Raso"),
 		("Machembrado","Machembrado"),
 		("Asbesto","Asbesto"),
 		
	)
	tipo_techop = models.CharField(max_length=100, choices=tipo_techo, null=True, blank=True)

	tenencia = (

		("Propio","Propio"),
 		("Alquilada","Alquilada"),
 		("Los Padres","Los Padres"),
 		("Prestada","Prestada"),
 		("Hacimaniento","hacimaniento"),	
	)
	tenencia = models.CharField(max_length=100, choices=tenencia, null=True, blank=True)

	aseourbano=models.BooleanField()
	electricidad=models.BooleanField()
	aguadepozo=models.BooleanField()
	cloacas=models.BooleanField()
	pozoseptico=models.BooleanField()
	fogon=models.BooleanField()
	gas=models.BooleanField()
	campoabierto=models.BooleanField()
	cisterna=models.BooleanField()
	




	def __str__(self):
		return '%s' %(self.id)
