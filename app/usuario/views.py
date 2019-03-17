from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

def RegPUser(request):
	if request.method == 'POST':
		form = PUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.puser.p_nombre = form.cleaned_data.get('p_nombre')
			user.puser.s_nombre = form.cleaned_data.get('s_nombre')
			user.puser.p_apellido = form.cleaned_data.get('p_apellido')
			user.puser.s_apellido = form.cleaned_data.get('s_apellido')
			user.puser.telefono = form.cleaned_data.get('telefono')
			user.puser.genero = form.cleaned_data.get('genero')
			user.puser.direccion = form.cleaned_data.get('direccion')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('/')
	else:
		form = PUserForm()
	return render(request, 'usuario/registro.html', {'users': form})

class Login(FormView):
	model = User
	form_class = AuthenticationForm
	template_name = "usuario/login.html"
 
	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, { 'form': form, 'message':'' })

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Inicio')
		else:
			mensaje= "El Usuario o la Contraseña son Incorrectos."
			return render(request, self.template_name, {'form':self.form_class ,'message':mensaje })

class LogoutView(FormView):
	def get(self, request):
		logout(request)
		return redirect('Inicio')

def EditarClave(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			logout(request)
			return redirect('Inicio')
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'usuario/editarclave.html', {"form": form})


def EditarPerfil(request):
	content = {}
	profile = request.user.get_username()
	print(profile)
	if request.method == 'POST':
		form1 = EditarPUserForm(request.POST, instance=request.user.puser)
		form2 = EditarPUserForm(request.POST, instance=request.user)
		content['form1'] = form1
		content['form2'] = form2
		if form1.is_valid() and form2.is_valid():
			usuario1 = form1.save()
			usuario2 = form2.save()
			return redirect("/")
	else:
		form1 = EditarPUserForm(instance=request.user.puser)
		form2 = EditarPUserForm(instance=request.user)
		content['form1'] = form1
		content['form2'] = form2
	return render(request, 'usuario/editarperfil.html', content)

def EditarAsignarCargo(request, pk):
	puser = get_object_or_404(PUser, pk=pk)
	if request.method == "POST":
		form = EditarPUserForm(request.POST, instance=puser)
		if form.is_valid():
			puser = form.save(commit=False)
			puser.save()
			return redirect('/')
		else:
			return render(request, "registro/asigcargo.html", {"cargo":form, "vpuser":puser})	
	else:
		form = EditarPUserForm(instance=puser)
	return render(request, "registro/asigcargo.html", {"cargo":form, "vpuser":puser})