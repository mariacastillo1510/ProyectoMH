import datetime
import time
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from app.registro.models import *
from django.views.generic.base import TemplateView

#Reportlab------------------------------------------------
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from datetime import date, time
import os
from io import BytesIO
from reportlab.platypus.tables import Table, TableStyle, CellStyle, LongTable
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter, A4,  LETTER, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, BaseDocTemplate, Frame, PageTemplate, Image, TableStyle, Spacer, SimpleDocTemplate, PageBreak
from reportlab.lib.units import inch, cm, mm 
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY

#importo models profile
from app.usuario.models import PUser
from django.http import JsonResponse
from django.contrib.staticfiles import finders

#SOLICITANTE----------------------------------------------------------
def ConsultarSolicitante(request):
	solicitante = PUser.objects.all()
	return render(request, "consulta/solicitante.html", {"solicitante": solicitante})

def VerSolicitante(request, pk):
	solicitante = get_object_or_404(PUser, pk=pk)
	return render(request, "consulta/ver_solicitante.html", {"solicitante":solicitante})

#CITA---------------------------------------------------------------------------
def ConsultarCita(request):
	cita = Cita.objects.all()
	return render(request, "consulta/cita.html", {"cita": cita})

def VerCita(request, pk):
	cita = get_object_or_404(Cita, pk=pk)
	return render(request, "consulta/ver_cita.html", {"cita":cita})

#SOLICITUDES---------------------------------------------------------------------
def ConsultarSolicitudes(request):
	solicitudes = Solicitudes.objects.all()
	return render(request, "consulta/solicitudes.html", {"solicitudes": solicitudes})

def VerSolicitudes(request, pk):
	solicitudes = get_object_or_404(Solicitudes, pk=pk)
	return render(request, "consulta/ver_solicitudes.html", {"solicitudes":solicitudes})

#TRABAJADOR---------------------------------------------------------------------
def ConsultarTrabajador(request):
	usuario = User.objects.all()
	return render(request, "consulta/trabajador.html", {"usuarios":usuario})
	
def ConsultarAsigCargo(request):
	usuario = User.objects.all()
	return render(request, "consulta/asigcargo.html", {"usuarios":usuario})

#Inspecciones --------------------------------------------------------------
def ConsultarInspeccion(request):
	inspeccion = Inspecciones.objects.all()
	return render(request, "consulta/inspeccion.html", {"inspeccion": inspeccion})

def VerInspecciones(request, pk):
	inspeccion = get_object_or_404(Inspecciones, pk=pk)
	print(inspeccion)
	return render(request, "consulta/ver_inspecciones.html", {"inspeccion":inspeccion})







#Numero de pagina
class NumberedCanvas(canvas.Canvas):
	def __init__(self, *args, **kwargs):
		canvas.Canvas.__init__(self, *args, **kwargs)
		self._saved_page_states = []
 
	def showPage(self):
		self._saved_page_states.append(dict(self.__dict__))
		self._startPage()
 
	def save(self):
		"""add page info to each page (page x of y)"""
		num_pages = len(self._saved_page_states)
		for state in self._saved_page_states:
			self.__dict__.update(state)
			self.draw_page_number(num_pages)
			canvas.Canvas.showPage(self)
		canvas.Canvas.save(self)
 
	def draw_page_number(self, page_count):
		self.setFont("Helvetica-Bold", 7)
		self.drawRightString(201 * mm, 4 * mm + (0.1 * inch),"Página %d de %d" % (self._pageNumber, page_count))

#PDF DE LAS CITAS
def HeaderFooterCita(canvas,doc):
		canvas.saveState()
		title = "Reporte de Citas - SolicitudeDV"
		canvas.setTitle(title)
		
		Story=[]
		styles = getSampleStyleSheet()
		
		archivo_imagen = finders.find('img/MDHV.png')
		canvas.drawImage(archivo_imagen, 30, 740, width=540,height=100,preserveAspectRatio=True)

		fecha = datetime.now().strftime('%d/%m/%Y ')
		# Estilos de Párrafos
		ta_c = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 11,
							fontName="Helvetica-Bold",
							)	
		ta_l = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)
		ta_l7 = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 7,
							fontName="Helvetica-Bold",
							)
		ta_r = ParagraphStyle('parrafos', 
							alignestt = TA_RIGHT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)

		# Header
		header = Paragraph("<u>REPORTE DE CITAS</u> ",ta_l,)
		w,h = header.wrap(doc.width-130, doc.topMargin)
		header.drawOn(canvas, 35, doc.height +10 + doc.topMargin - 10)

		header1 = Paragraph("<u>MINISTERIO DE HÁBITAT Y VIVIENDA</u> ",ta_r,)
		w,h = header1.wrap(doc.width-115, doc.topMargin)
		header1.drawOn(canvas, 180, doc.height +40 + doc.topMargin - 2)

		P1 = Paragraph('''<b>N°</b>''',ta_c)
		P2 = Paragraph('''<b>SOLICITUD</b>''',ta_c)
		P3 = Paragraph('''<b>FECHA</b>''',ta_c)
		P4 = Paragraph('''<b>HORA</b>''',ta_c)
		P5 = Paragraph('''<b>TRABAJADOR</b>''',ta_c)
		data= [[P1, P2, P3, P4, P5]]
		header2 = Table(data, colWidths = [35,85,80,80,255])
		header2.setStyle(TableStyle( 
			[	
				('GRID', (0, -1), (-1, -1), 1, colors.black),
				('BACKGROUND', (0, 0), (-1, 0), colors.lightyellow)
			]
			))
		w,h = header2.wrap(doc.width-115, doc.topMargin)
		header2.drawOn(canvas, 30, doc.height +5 + doc.topMargin - 40)

		# Llamado del Modelo Director
		#director = get_object_or_404(Director)

		#if director.sexo == "Feestino":
		#	sexo = "DIRECTORA"
		#else:
		#	sexo = "DIRECTOR"

		# FOOTER
		footer = Paragraph("Atentamente,",ta_c)
		w, h = footer.wrap(doc.width -125, doc.bottomMargin -275) 
		footer.drawOn(canvas, doc.height -245, doc.topMargin +35, h)

		footer1 = Paragraph("_______________________________",ta_c)
		w, h = footer1.wrap(doc.width -115, doc.bottomMargin - 15) 
		footer1.drawOn(canvas, doc.height -300, doc.topMargin -1, w)

		footer2 = Paragraph("Luis R" + " Jiménez R",ta_c)
		w, h = footer2.wrap(doc.width -240, doc.bottomMargin -275) 
		footer2.drawOn(canvas,doc.height -255, doc.topMargin -15, h)

		footer3 = Paragraph("Director Estadal"+" De  Hábitat" + " y Vivienda",ta_c)
		w, h = footer3.wrap(doc.width -250, doc.bottomMargin) 
		footer3.drawOn(canvas,doc.height -315, doc.topMargin -30, h)

		footer4 = Paragraph("Del Estado "+"Portuguesa",ta_c)
		w, h = footer4.wrap(doc.width -300, doc.bottomMargin) 
		footer4.drawOn(canvas,doc.height -275, doc.topMargin -45, h)

		footer5 = Paragraph("Publicada en gaceta oficial Nº "+ " 41.356 " + " de fecha 08/03/2018",ta_c)
		w, h = footer5.wrap(doc.width -200, doc.bottomMargin) 
		footer5.drawOn(canvas,doc.height -355, doc.topMargin -60, h)

		footer6 = Paragraph("Designada mendiante resolución Nº"+" 055 de fecha 06/03/2018",ta_c)
		w, h = footer6.wrap(doc.width -150, doc.bottomMargin) 
		footer6.drawOn(canvas,doc.height -360, doc.topMargin -75, h)

		footer7 = Paragraph("Fecha de expedición: "+str(fecha),ta_l7)
		w, h = footer7.wrap(doc.width -200, doc.bottomMargin) 
		footer7.drawOn(canvas,doc.height -490, doc.topMargin -165, h)

		canvas.restoreState()

def CitasPDF(request):
	response = HttpResponse(content_type='application/pdf')
	buffer = BytesIO()
	pdf = canvas.Canvas(buffer)
	doc = SimpleDocTemplate(buffer,
		pagesizes=letter,
		rightMargin = 30,
		leftMargin= 30,
		topMargin=180,
		bottomMargin=150,
		paginate_by=0,
	)

	citas=[]
	styles = getSampleStyleSheet()
	# ESTILO DE PÁRAGRAFOS
	ta_l8HU = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	# TABLA NUMERO 1
	
	data = [(Cita.id,Cita.solicitud.numero_de_oficio, Cita.fecha, Cita.hora, Cita.trabajador) for Cita in Cita.objects.all()]
	x = Table(data, colWidths = [35,85,80,80,255])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (12, -1), 1, colors.black),
			('ALIGN',(0,0),(3,-1),'CENTER'),
			('FONTSIZE', (0, 0), (4, -1), 8),	
		]
	))
	citas.append(x)

	doc.build(citas,onFirstPage=HeaderFooterCita,onLaterPages=HeaderFooterCita,canvasmaker=NumberedCanvas)
	response.write(buffer.getvalue())
	buffer.close()
	return response

#PDF CITA INDIVIDUAL
def HeaderFooterCitaIndividual(canvas,doc):
		canvas.saveState()
		title = "Reporte de Cita - Vivienda"
		canvas.setTitle(title)
		
		Story=[]
		styles = getSampleStyleSheet()
		
		archivo_imagen = "static/img/MDHV.png"
		canvas.drawImage(archivo_imagen, 30, 740, width=540,height=100,preserveAspectRatio=True)

		fecha = datetime.now().strftime('%d/%m/%Y ')
		# Estilos de Párrafos
		ta_c = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 11,
							fontName="Helvetica-Bold",
							)	
		ta_l = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)
		ta_l7 = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 7,
							fontName="Helvetica-Bold",
							)
		ta_r = ParagraphStyle('parrafos', 
							alignestt = TA_RIGHT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)

		# Header
		header = Paragraph("<u>REPORTE DE CITAS</u> ",ta_l,)
		w,h = header.wrap(doc.width-130, doc.topMargin)
		header.drawOn(canvas, 100, doc.height +20 + doc.topMargin - 2)

		header1 = Paragraph("<u>MINISTERIO DE HÁBITAT Y VIVIENDA</u> ",ta_r,)
		w,h = header1.wrap(doc.width-115, doc.topMargin)
		header1.drawOn(canvas, 175, doc.height +65 + doc.topMargin - 5)

		# Llamado del Modelo Director
		#director = get_object_or_404(Director)

		#if director.sexo == "Feestino":
		#	sexo = "DIRECTORA"
		#else:
		#	sexo = "DIRECTOR"

		# FOOTER
		footer = Paragraph("Atentamente,",ta_c)
		w, h = footer.wrap(doc.width -125, doc.bottomMargin -275) 
		footer.drawOn(canvas, doc.height -245, doc.topMargin +35, h)

		footer1 = Paragraph("_______________________________",ta_c)
		w, h = footer1.wrap(doc.width -115, doc.bottomMargin - 15) 
		footer1.drawOn(canvas, doc.height -300, doc.topMargin -1, w)

		footer2 = Paragraph("Luis R" + " Jiménez R",ta_c)
		w, h = footer2.wrap(doc.width -240, doc.bottomMargin -275) 
		footer2.drawOn(canvas,doc.height -255, doc.topMargin -15, h)

		footer3 = Paragraph("Director Estadal"+" De  Hábitat" + " y Vivienda",ta_c)
		w, h = footer3.wrap(doc.width -250, doc.bottomMargin) 
		footer3.drawOn(canvas,doc.height -315, doc.topMargin -30, h)

		footer4 = Paragraph("Del Estado "+"Portuguesa",ta_c)
		w, h = footer4.wrap(doc.width -300, doc.bottomMargin) 
		footer4.drawOn(canvas,doc.height -275, doc.topMargin -45, h)

		footer5 = Paragraph("Publicada en gaceta oficial Nº "+ " 41.356 " + " de fecha 08/03/2018",ta_c)
		w, h = footer5.wrap(doc.width -200, doc.bottomMargin) 
		footer5.drawOn(canvas,doc.height -355, doc.topMargin -60, h)

		footer6 = Paragraph("Designada mendiante resolución Nº"+" 055 de fecha 06/03/2018",ta_c)
		w, h = footer6.wrap(doc.width -150, doc.bottomMargin) 
		footer6.drawOn(canvas,doc.height -360, doc.topMargin -75, h)

		footer6 = Paragraph("Fecha de expedición: "+str(fecha),ta_l7)
		w, h = footer6.wrap(doc.width -200, doc.bottomMargin) 
		footer6.drawOn(canvas,doc.height -490, doc.topMargin -159, h)

		canvas.restoreState()

def CitaIndividualPDF(request, cita_id):
	response = HttpResponse(content_type='application/pdf')
	buffer = BytesIO()
	pdf = canvas.Canvas(buffer)
	doc = SimpleDocTemplate(buffer,
		pagesizes=letter,
		rightMargin = 30,
		leftMargin= 30,
		topMargin=170,
		bottomMargin=170,
		paginate_by=0,
	)

	cita=[]
	styles = getSampleStyleSheet()
	# ESTILO DE PÁRAGRAFOS
	ta_cBold8 = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	ta_l8HU = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	# LLAMADO DEL MODELO
	citas = get_object_or_404(Cita, id=cita_id)

	P0 = Paragraph('''<b>CITA</b>''',ta_cBold8)
	P1 = Paragraph('''<b>NUMERO DE OFICIO</b>''',ta_cBold8)
	P2 = Paragraph(str(citas.solicitud),ta_l8HU)
	P3 = Paragraph('''<b>SOLICITANTE</b>''',ta_cBold8)
	P4 = Paragraph(str(citas.solicitante),ta_l8HU)
	P5 = Paragraph('''<b>FECHA</b>''',ta_cBold8)
	P6 = Paragraph(str(citas.fecha),ta_l8HU)
	P7 = Paragraph('''<b>HORA</b>''',ta_cBold8)
	P8 = Paragraph(str(citas.hora),ta_l8HU)
	P9 = Paragraph('''<b>TRABAJADOR</b>''',ta_cBold8)
	P10 = Paragraph(str(citas.trabajador),ta_l8HU)
	#P9 = Paragraph('''<b>INSPECCIÓN REALIZADA</b>''',ta_cBold8)
	#if citas.citass == True:
	#	citass = "SI"
	#else:
	#	citass = "NO"
	#P10 = Paragraph(str(citass),ta_l8HU)
	
	# TABLA NUMERO 1
	data= [[P0]]
	x = Table(data, colWidths = [400])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BACKGROUND', (0, 0), (0, 1), colors.lightyellow),
			('BOX',(0,0),(0,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),	
		]
	))
	cita.append(x)

	# TABLA NUMERO 2
	data= [[P1,P2],[P3,P4],[P5,P6],[P7,P8],[P9,P10]]
	x = Table(data, colWidths = [200,200])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BOX',(0,0),(1,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),
			('VALIGN',(0,0),(0,-1),'CENTER'),

		]
	))
	cita.append(x)

	doc.build(cita,onFirstPage=HeaderFooterCitaIndividual,onLaterPages=HeaderFooterCitaIndividual,canvasmaker=NumberedCanvas)
	response.write(buffer.getvalue())
	buffer.close()

	return response	

#pdf de la inspecciones
def HeaderFooterInspeccionIndividual(canvas,doc):
		canvas.saveState()
		title = "Reporte de inspeccion - Vivienda"
		canvas.setTitle(title)
		
		Story=[]
		styles = getSampleStyleSheet()
		
		archivo_imagen = "static/img/MDHV.png"
		canvas.drawImage(archivo_imagen, 30, 740, width=540,height=100,preserveAspectRatio=True)

		fecha = datetime.now().strftime('%d/%m/%Y ')
		# Estilos de Párrafos
		ta_c = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 11,
							fontName="Helvetica-Bold",
							)	
		ta_l = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)
		ta_l7 = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 7,
							fontName="Helvetica-Bold",
							)
		ta_r = ParagraphStyle('parrafos', 
							alignestt = TA_RIGHT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)

		# FOOTER
		footer = Paragraph("Atentaestte,",ta_c)
		w, h = footer.wrap(doc.width -125, doc.bottomMargin -275) 
		footer.drawOn(canvas, doc.height -420, doc.topMargin +15, h)

		footer1 = Paragraph("___________________________",ta_c)
		w, h = footer1.wrap(doc.width -115, doc.bottomMargin - 15) 
		footer1.drawOn(canvas, doc.height -430, doc.topMargin -15, w)

		footer2 = Paragraph("Limber" + " Monsalve",ta_c)
		w, h = footer2.wrap(doc.width -240, doc.bottomMargin -275) 
		footer2.drawOn(canvas,doc.height -365, doc.topMargin -30, h)

		footer3 = Paragraph("COORDINADOR"+" DE PAA",ta_c)
		w, h = footer3.wrap(doc.width -300, doc.bottomMargin) 
		footer3.drawOn(canvas,doc.height -336, doc.topMargin -45, h)

		footer4 = Paragraph("Según Resolución N°"+"1234",ta_c)
		w, h = footer4.wrap(doc.width -300, doc.bottomMargin) 
		footer4.drawOn(canvas,doc.height -338, doc.topMargin -60, h)

		footer5 = Paragraph("De Fecha "+"2017",ta_c)
		w, h = footer5.wrap(doc.width -300, doc.bottomMargin) 
		footer5.drawOn(canvas,doc.height -340, doc.topMargin -75, h)

		footer6 = Paragraph("Fecha de expedición: "+str(fecha),ta_l7)
		w, h = footer6.wrap(doc.width -200, doc.bottomMargin) 
		footer6.drawOn(canvas,doc.height -510, doc.topMargin -139, h)

		canvas.restoreState()

def InspeccionIndividualPDF(request, inspeccion_id):
	response = HttpResponse(content_type='application/pdf')
	buffer = BytesIO()
	pdf = canvas.Canvas(buffer)
	doc = SimpleDocTemplate(buffer,
		pagesizes=letter,
		rightMargin = 30,
		leftMargin= 30,
		topMargin=75,
		bottomMargin=170,
		paginate_by=0,
	)

	inspeccion=[]
	styles = getSampleStyleSheet()
	# ESTILO DE PÁRAGRAFOS
	ta_cBold8 = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	ta_l8HU = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	# LLAMADO DEL MODELO
	inspecciones = get_object_or_404(Inspecciones, id=inspeccion_id)

	# TABLA NUMERO 1
	data = [["ABORDAJE SOCIOECONOMICO"]]
	x = Table(data, colWidths = [505])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BACKGROUND', (0, 0), (0, 1), colors.lightyellow),
			('BOX',(0,0),(0,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'CENTER'),
		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 2
	data= [["Fecha:          /            /          "]]
	x = Table(data, colWidths = [505])
	x.setStyle(TableStyle(
		[	
			('FONTSIZE', (0, 0), (0, -1), 8),	
			('ALIGN',(0,0),(0,-1),'RIGHT'),
		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 3
	data= [["Tipo de Solicitud: ","123"]]
	x = Table(data, colWidths = [70,435])
	x.setStyle(TableStyle(
		[	
			('BOX',(0,0),(1,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (1, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 4
	data = [["IDENTIFICACIÓN DEL SOLICITANTE"]]
	x = Table(data, colWidths = [505])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BACKGROUND', (0, 0), (0, 1), colors.lightyellow),
			('BOX',(0,0),(0,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'CENTER'),
		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 5
	data= [["Apellidos y Nombres: ","123","C.I N°","sss"]]
	x = Table(data, colWidths = [90,265,50,100])
	x.setStyle(TableStyle(
		[	
			('GRID', (4, 0), (1, -1), 1, colors.black),
			('BOX',(0,0),(3,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (3, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 6
	data= [["Lugar de Nacimiento: ","123","Fecha de Nacimiento: ","14/03/2019","Edad:","sss"]]
	x = Table(data, colWidths = [90,195,105,60,30,25])
	x.setStyle(TableStyle(
		[	
			('GRID', (4, 0), (1, -1), 1, colors.black),
			('BOX',(0,0),(5,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (5, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 7
	data= [["Estado Civil: ","Soltero( )","Casado( )","Concubinato( )","Divorciado( )","Sexo:","F( )","M( )","Nacionalidad","V( )","E( )"]]
	x = Table(data, colWidths = [50,40,40,60,70,30,25,50,80,30,30])
	x.setStyle(TableStyle(
		[	
			('GRID', (-3, 0), (4, -1), 1, colors.black),
			('BOX',(0,0),(10,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (10, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)

	# TABLA NUMERO 8
	data= [["Nivel de Instruccion: ","123","Profeion/Ocupacion: ","14","Trabaja:","Si()","No()"]]
	x = Table(data, colWidths = [90,120,105,90,40,30,30])
	x.setStyle(TableStyle(
		[	
			('GRID', (4, 0), (1, -1), 1, colors.black),
			('BOX',(0,0),(6,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (6, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)

	# TABLA NUMERO 9
	data= [["Donde Trabaja: ","123","Ingreso Famiiar:","213","Censo GMVV:","S( )","N( )","Censo 0800:","456",]]
	x = Table(data, colWidths = [80,60,40,60,70,30,35,50,80,])
	x.setStyle(TableStyle(
		[	
			('GRID', (-3, 0), (4, -1), 1, colors.black),
			('BOX',(0,0),(8,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (8, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)

	# TABLA NUMERO 10
	data = [["DIRECCIÓN DE HABITACIÓN"]]
	x = Table(data, colWidths = [505])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BACKGROUND', (0, 0), (0, 1), colors.lightyellow),
			('BOX',(0,0),(0,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'CENTER'),
		]
	))
	inspeccion.append(x)

	# TABLA NUMERO 11
	data= [["Urbanización o Barrio: ","123","Av.","__","Esq.","__","Calle.","__","Vda.","__","Sector","525","Número de Casa","241"]]
	x = Table(data, colWidths = [80,145,15,15,15,15,25,15,15,15,30,25,70,25])
	x.setStyle(TableStyle(
		[	
			('GRID', (-2, 0), (1, -1), 1, colors.black),
			('BOX',(0,0),(13,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (13, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)

	# TABLA NUMERO 12
	data= [["Ciudad: ","123","Parroquia: ","jjj","Municipio:","sss"]]
	x = Table(data, colWidths = [69,100,68,100,68,100])
	x.setStyle(TableStyle(
		[	
			('GRID', (4, 0), (1, -1), 1, colors.black),
			('BOX',(0,0),(5,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (5, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 13
	data= [["Estado: ","123","Telefono de Habitacion: ","jjj","Telefono Celular:","sss"]]
	x = Table(data, colWidths = [69,100,88,80,68,100])
	x.setStyle(TableStyle(
		[	
			('GRID', (4, 0), (1, -1), 1, colors.black),
			('BOX',(0,0),(5,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (5, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 14
	data = [["DESCRIPCION DE LA VIVIENDA"]]
	x = Table(data, colWidths = [505])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BACKGROUND', (0, 0), (0, 1), colors.lightyellow),
			('BOX',(0,0),(0,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'CENTER'),
		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 15
	data= [[" ","Casa","( )","Rural","( )","Rancho","( )","Apto","( )","Quinta","( )","Barraca","( )","Tabla","( )","Otro","( )", " "]]
	x = Table(data, colWidths = [85,25,15,25,15,30,15,25,15,30,15,30,15,25,15,25,15,85])
	x.setStyle(TableStyle(
		[	
			('BOX',(0,0),(17,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (17, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 16
	data = [["TIPO DE PARED"]]
	x = Table(data, colWidths = [505])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.grey),
			('BACKGROUND', (0, 0), (0, 1), colors.lightyellow),
			('BOX',(0,0),(0,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (0, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'CENTER'),
		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 17
	data= [[" ","Frisada","( )","Sin Frizar","( )","Barharete","( )","Adobe","( )","Zing","( )","Tabla","( )","Carton","( )","Carton Piedra","( )" ,"Otros","( )"," "]]
	x = Table(data, colWidths = [47,30,15,37,15,37,15,25,15,17,15,25,15,25,15,55,15,25,15,47])
	x.setStyle(TableStyle(
		[	
			('BOX',(0,0),(19,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (19, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 18
	data= [[" ","Cemento","( )","Rustico","( )","Tierra","( )","Baldosa","( )","Granito","( )","Cemento Pulido","( )","Otro","( )", " "]]
	x = Table(data, colWidths = [85,35,15,30,15,25,15,30,15,30,15,60,15,20,15,85])
	x.setStyle(TableStyle(
		[	
			('BOX',(0,0),(15,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (15, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 19
	data= [[" ","Acerojil","( )","Zing","( )","Platabanda","( )","Tejas","( )","Raso","( )","Machihenbrado","( )","Asbesto","( )","Otro","( )", " "]]
	x = Table(data, colWidths = [65,30,15,20,15,45,15,25,15,25,15,55,15,30,15,25,15,65])
	x.setStyle(TableStyle(
		[	
			('BOX',(0,0),(17,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (17, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
	# TABLA NUMERO 20
	data = [["TENENCIA","SERVICIOS BASICOS"]]
	x = Table(data, colWidths = [252.5,252.5])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (1, -1), 0.1, colors.black),
			('BACKGROUND', (0, 0), (1, 1), colors.lightyellow),
			('BOX',(0,0),(1,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (1, -1), 8),
			('ALIGN',(0,0),(1,-1),'CENTER'),
		]
	))
	inspeccion.append(x)
# TABLA NUMERO 21
	data= [["","Propia","( )","Alquilada","( )","Invadida","( )","","","Aceo Urbano","( )","Pozo Septico","( )","Cloacas","( )", " "]]
	x = Table(data, colWidths = [55,25,15,35,15,35,15,58,39,50,15,50,15,30,15,38])
	x.setStyle(TableStyle(
		[	
			('GRID', (8, 0), (7, -1), 0.1, colors.black),
			('BOX',(0,0),(15,-1), 1,colors.black),
			('FONTSIZE', (0, 0), (15, -1), 8),
			('ALIGN',(-1,-1),(-1,-1),'LEFT'),

		]
	))
	inspeccion.append(x)
























	doc.build(inspeccion,onFirstPage=HeaderFooterInspeccionIndividual,onLaterPages=HeaderFooterInspeccionIndividual,canvasmaker=NumberedCanvas)
	response.write(buffer.getvalue())
	buffer.close()

	return response	

#PDF SOLICITANTE 
def HeaderFooterSolicitante(canvas,doc):
		canvas.saveState()
		title = "Reporte de Solicitante - SolicitudeDV"
		canvas.setTitle(title)
		
		Story=[]
		styles = getSampleStyleSheet()
		
		archivo_imagen = finders.find('img/MDHV.png')
		canvas.drawImage(archivo_imagen, 30, 740, width=540,height=100,preserveAspectRatio=True)

		fecha = datetime.now().strftime('%d/%m/%Y ')
		# Estilos de Párrafos
		ta_c = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 11,
							fontName="Helvetica-Bold",
							)	
		ta_l = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)
		ta_l7 = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 7,
							fontName="Helvetica-Bold",
							)
		ta_r = ParagraphStyle('parrafos', 
							alignestt = TA_RIGHT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)

		# Header
		header = Paragraph("<u>REPORTE DE LOS USUARIOS</u> ",ta_l,)
		w,h = header.wrap(doc.width-130, doc.topMargin)
		header.drawOn(canvas, 35, doc.height +10 + doc.topMargin - 25)

		header1 = Paragraph("<u>MINISTERIO DE HÁBITAT Y VIVIENDA</u> ",ta_r,)
		w,h = header1.wrap(doc.width-115, doc.topMargin)
		header1.drawOn(canvas, 180, doc.height +40 + doc.topMargin - 2)

		P1 = Paragraph('''<b>N°</b>''',ta_c)
		P2 = Paragraph('''<b>CÉDULA</b>''',ta_c)
		P3 = Paragraph('''<b>NOMBRE</b>''',ta_c)
		P4 = Paragraph('''<b>APELLIDO</b>''',ta_c)
		P5 = Paragraph('''<b>TELEFONO</b>''',ta_c)
		P6 = Paragraph('''<b>CORREO ELECTRÓNICO</b>''',ta_c)

		data= [[P1, P2, P3, P4, P5, P6]]
		header2 = Table(data, colWidths = [35,85,80,80,80,170])
		header2.setStyle(TableStyle( 
			[	
				('GRID', (0, -1), (-1, -1), 1, colors.black),
				('BACKGROUND', (0, 0), (-1, 0), colors.lightyellow)
			]
			))
		w,h = header2.wrap(doc.width-115, doc.topMargin)
		header2.drawOn(canvas, 30, doc.height +5 + doc.topMargin - 60)

		# Llamado del Modelo Director
		#director = get_object_or_404(Director)

		#if director.sexo == "Feestino":
		#	sexo = "DIRECTORA"
		#else:
		#	sexo = "DIRECTOR"

		# FOOTER
		footer = Paragraph("Atentamente,",ta_c)
		w, h = footer.wrap(doc.width -125, doc.bottomMargin -275) 
		footer.drawOn(canvas, doc.height -230, doc.topMargin +35, h)

		footer1 = Paragraph("_______________________________",ta_c)
		w, h = footer1.wrap(doc.width -120, doc.bottomMargin - 15) 
		footer1.drawOn(canvas, doc.height -290, doc.topMargin -1, w)

		footer2 = Paragraph("Luis R" + " Jiménez R",ta_c)
		w, h = footer2.wrap(doc.width -240, doc.bottomMargin -275) 
		footer2.drawOn(canvas,doc.height -240, doc.topMargin -15, h)

		footer3 = Paragraph("Director Estadal"+" De  Hábitat" + " y Vivienda",ta_c)
		w, h = footer3.wrap(doc.width -250, doc.bottomMargin) 
		footer3.drawOn(canvas,doc.height -290, doc.topMargin -30, h)

		footer4 = Paragraph("Del Estado "+"Portuguesa",ta_c)
		w, h = footer4.wrap(doc.width -300, doc.bottomMargin) 
		footer4.drawOn(canvas,doc.height -250, doc.topMargin -45, h)

		footer5 = Paragraph("Publicada en gaceta oficial Nº "+ " 41.356 " + " de fecha 08/03/2018",ta_c)
		w, h = footer5.wrap(doc.width -200, doc.bottomMargin) 
		footer5.drawOn(canvas,doc.height -355, doc.topMargin -60, h)

		footer6 = Paragraph("Designada mendiante resolución Nº"+" 055 de fecha 06/03/2018",ta_c)
		w, h = footer6.wrap(doc.width -150, doc.bottomMargin) 
		footer6.drawOn(canvas,doc.height -360, doc.topMargin -75, h)

		footer7 = Paragraph("Fecha de expedición: "+str(fecha),ta_l7)
		w, h = footer7.wrap(doc.width -200, doc.bottomMargin) 
		footer7.drawOn(canvas,doc.height -470, doc.topMargin -185, h)

		canvas.restoreState()

def SolicitantePDF(request):
	response = HttpResponse(content_type='application/pdf')
	buffer = BytesIO()
	pdf = canvas.Canvas(buffer)
	doc = SimpleDocTemplate(buffer,
		pagesizes=letter,
		rightMargin = 35,
		leftMargin= 29,
		topMargin=200,
		bottomMargin=150,
		paginate_by=0,
	)

	puser=[]
	styles = getSampleStyleSheet()
	# ESTILO DE PÁRAGRAFOS
	ta_l8HU = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	# TABLA NUMERO 1
	
	data = [(PUser.id,PUser.user, PUser.p_nombre, PUser.p_apellido, PUser.telefono, PUser.user.email) for PUser in PUser.objects.all()]
	x = Table(data, colWidths = [35,85,80,80,80,170])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (15, -1), 1, colors.black),
			('ALIGN',(0,0),(3,-1),'CENTER'),
			('FONTSIZE', (0, 0), (5, -1), 8),	
		]
	))
	puser.append(x)

	doc.build(puser,onFirstPage=HeaderFooterSolicitante,onLaterPages=HeaderFooterSolicitante,canvasmaker=NumberedCanvas)
	response.write(buffer.getvalue())
	buffer.close()
	return response

#pdf del solicitante individual <----------falta



#PDF DE LA SOLICITUDES 
def HeaderFooterSolicitudes(canvas,doc):
		canvas.saveState()
		title = "Reporte de las solicitudes - SolicitudeDV"
		canvas.setTitle(title)
		
		Story=[]
		styles = getSampleStyleSheet()
		
		archivo_imagen = finders.find('img/MDHV.png')
		canvas.drawImage(archivo_imagen, 30, 740, width=540,height=100,preserveAspectRatio=True)

		fecha = datetime.now().strftime('%d/%m/%Y ')
		# Estilos de Párrafos
		ta_c = ParagraphStyle('parrafos', 
							alignestt = TA_CENTER,
							fontSize = 11,
							fontName="Helvetica-Bold",
							)	
		ta_l = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)
		ta_l7 = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 7,
							fontName="Helvetica-Bold",
							)
		ta_r = ParagraphStyle('parrafos', 
							alignestt = TA_RIGHT,
							fontSize = 13,
							fontName="Helvetica-Bold",
							)

		# Header
		header = Paragraph("<u>REPORTE DE LAS SOLICITUDES</u> ",ta_l,)
		w,h = header.wrap(doc.width-130, doc.topMargin)
		header.drawOn(canvas, 35, doc.height +10 + doc.topMargin - 25)

		header1 = Paragraph("<u>MINISTERIO DE HÁBITAT Y VIVIENDA</u> ",ta_r,)
		w,h = header1.wrap(doc.width-115, doc.topMargin)
		header1.drawOn(canvas, 180, doc.height +40 + doc.topMargin - 2)

		P1 = Paragraph('''<b>N°</b>''',ta_c)
		P2 = Paragraph('''<b>NUMERO DE OFICIO</b>''',ta_c)
		P3 = Paragraph('''<b>SOLICITANTE</b>''',ta_c)
		P4 = Paragraph('''<b>FECHA</b>''',ta_c)
		data= [[P1, P2, P3, P4]]
		header2 = Table(data, colWidths = [35,150,150,80,255])
		header2.setStyle(TableStyle( 
			[	
				('GRID', (0, -1), (-1, -1), 1, colors.black),
				('BACKGROUND', (0, 0), (-1, 0), colors.lightyellow)
			]
			))
		w,h = header2.wrap(doc.width-115, doc.topMargin)
		header2.drawOn(canvas, 75, doc.height +5 + doc.topMargin - 60)

		# Llamado del Modelo Director
		#director = get_object_or_404(Director)

		#if director.sexo == "Feestino":
		#	sexo = "DIRECTORA"
		#else:
		#	sexo = "DIRECTOR"

		# FOOTER
		footer = Paragraph("Atentamente,",ta_c)
		w, h = footer.wrap(doc.width -125, doc.bottomMargin -275) 
		footer.drawOn(canvas, doc.height -230, doc.topMargin +35, h)

		footer1 = Paragraph("_______________________________",ta_c)
		w, h = footer1.wrap(doc.width -120, doc.bottomMargin - 15) 
		footer1.drawOn(canvas, doc.height -290, doc.topMargin -1, w)

		footer2 = Paragraph("Luis R" + " Jiménez R",ta_c)
		w, h = footer2.wrap(doc.width -240, doc.bottomMargin -275) 
		footer2.drawOn(canvas,doc.height -240, doc.topMargin -15, h)

		footer3 = Paragraph("Director Estadal"+" De  Hábitat" + " y Vivienda",ta_c)
		w, h = footer3.wrap(doc.width -250, doc.bottomMargin) 
		footer3.drawOn(canvas,doc.height -290, doc.topMargin -30, h)

		footer4 = Paragraph("Del Estado "+"Portuguesa",ta_c)
		w, h = footer4.wrap(doc.width -300, doc.bottomMargin) 
		footer4.drawOn(canvas,doc.height -250, doc.topMargin -45, h)

		footer5 = Paragraph("Publicada en gaceta oficial Nº "+ " 41.356 " + " de fecha 08/03/2018",ta_c)
		w, h = footer5.wrap(doc.width -200, doc.bottomMargin) 
		footer5.drawOn(canvas,doc.height -355, doc.topMargin -60, h)

		footer6 = Paragraph("Designada mendiante resolución Nº"+" 055 de fecha 06/03/2018",ta_c)
		w, h = footer6.wrap(doc.width -150, doc.bottomMargin) 
		footer6.drawOn(canvas,doc.height -360, doc.topMargin -75, h)

		footer7 = Paragraph("Fecha de expedición: "+str(fecha),ta_l7)
		w, h = footer7.wrap(doc.width -200, doc.bottomMargin) 
		footer7.drawOn(canvas,doc.height -470, doc.topMargin -185, h)

		canvas.restoreState()

def SolicitudesPDF(request):
	response = HttpResponse(content_type='application/pdf')
	buffer = BytesIO()
	pdf = canvas.Canvas(buffer)
	doc = SimpleDocTemplate(buffer,
		pagesizes=letter,
		rightMargin = 60,
		leftMargin= 30,
		topMargin=200,
		bottomMargin=150,
		paginate_by=0,
	)

	solicitudes=[]
	styles = getSampleStyleSheet()
	# ESTILO DE PÁRAGRAFOS
	ta_l8HU = ParagraphStyle('parrafos', 
							alignestt = TA_LEFT,
							fontSize = 8,
							fontName="Helvetica",
							textTransform = 'uppercase'
							)
	# TABLA NUMERO 1
	
	data = [(Solicitudes.id,Solicitudes.numero_de_oficio, Solicitudes.solicitante, Solicitudes.fecha) for Solicitudes in Solicitudes.objects.all()]
	x = Table(data, colWidths = [35,150,150,80,255])
	x.setStyle(TableStyle(
		[	
			('GRID', (0, 0), (12, -1), 1, colors.black),
			('ALIGN',(0,0),(3,-1),'CENTER'),
			('FONTSIZE', (0, 0), (3, -1), 8),	
		]
	))
	solicitudes.append(x)

	doc.build(solicitudes,onFirstPage=HeaderFooterSolicitudes,onLaterPages=HeaderFooterSolicitudes,canvasmaker=NumberedCanvas)
	response.write(buffer.getvalue())
	buffer.close()
	return response




