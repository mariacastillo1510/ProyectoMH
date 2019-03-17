from django.conf.urls import url
from .views import *

urlpatterns = [
	#SOLICITANTE--------------------------------------------------------------
    url(r'^solicitante/$', ConsultarSolicitante, name='ConsultarSolicitante'),
    url(r'^solicitante/(?P<pk>[0-9]+)/$', VerSolicitante, name="VerSolicitante"),
    #CITAS-----------------------------------------------------------------------
    url(r'^cita/$', ConsultarCita, name='ConsultarCita'),
    url(r'^cita/(?P<pk>[0-9]+)/$', VerCita, name="VerCita"),
    #SOLICITUDES------------------------------------------------------------
    url(r'^solicitudes/$', ConsultarSolicitudes, name='ConsultarSolicitudes'),
    url(r'^solicitudes/(?P<pk>[0-9]+)/$', VerSolicitudes, name="VerSolicitudes"),
    #TRABAJADOR---------------------------------------------------------------------
    url(r'^trabajadores/$', ConsultarTrabajador, name="ConsultarTrabajador"),
    url(r'^asignarcargo/$', ConsultarAsigCargo, name='ConsultarAsigCargo'),

    #CitasPDF--------------------------------------------------------------------
    url(r'^citasPDF/$', CitasPDF, name='CitasPDF'),
    url(r'^citasPDF-(?P<cita_id>[0-9]+)/$', CitaIndividualPDF, name='cita_pdf'),

    #SolicitantePDF
    url(r'^solicitantePDF/$', SolicitantePDF, name='SolicitantePDF'),
    
    #Inspecciones registros -------------------------------------------------
    url(r'^inspeccion/$', ConsultarInspeccion, name='ConsultarInspeccion'),
    url(r'^inspeccion/(?P<pk>[0-9]+)/$', VerInspecciones, name="VerInspecciones"),
    url(r'^inspeccionPDF-(?P<inspeccion_id>[0-9]+)/$', InspeccionIndividualPDF, name='inspeccion_pdf'),

    #SolicitudesPDF
    url(r'^solicitudesPDF/$', SolicitudesPDF, name='SolicitudesPDF'),
]