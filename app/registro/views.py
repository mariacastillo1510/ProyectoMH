from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,TemplateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *

def RSolicitudes(request):
	if request.method == 'POST':
		form = SolicitudesForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('Inicio')
	else:
		form = SolicitudesForm()
	return render(request,'registro/solicitudes.html',{'solicitudes':form})

def ESolicitudes(request,pk):
	solicitudes = get_object_or_404(Solicitudes, pk=pk)
	if request.method == "POST":
		form = SolicitudesForm(request.POST, instance=solicitudes)
		if form.is_valid():
			solicitudes = form.save(commit=False)
			solicitudes.save()
			return redirect('Consulta:ConsultarSolicitudes')
		else:
			return render(request, "ediciones/solicitudes.html", {"esoli":form, "vsoli":solicitudes})	
	else:
		form = SolicitudesForm(instance=solicitudes)
	return render(request, "ediciones/solicitudes.html", {"esoli":form, "vsoli":solicitudes})

def RCita(request):
	if request.method == 'POST':
		form = CitaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('Inicio')
	else:
		form = CitaForm()
	return render(request,'registro/citas.html',{'citas':form})

def ECita(request,pk):
	cita = get_object_or_404(Cita, pk=pk)
	if request.method == "POST":
		form = CitaForm(request.POST, instance=cita)
		if form.is_valid():
			cita = form.save(commit=False)
			cita.save()
			return redirect('Consulta:ConsultarCita')
		else:
			return render(request, "ediciones/cita.html", {"ecita":form, "vcita":cita})	
	else:
		form = CitaForm(instance=cita)
	return render(request, "ediciones/cita.html", {"ecita":form, "vcita":cita})