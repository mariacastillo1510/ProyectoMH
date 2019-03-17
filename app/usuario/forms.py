from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class PUserForm(UserCreationForm):
	nacio = (
		("V","V"),
		("E","E"),
	)
	nacionalidad = forms.ChoiceField(choices=nacio)
	p_nombre = forms.CharField(max_length=40)
	s_nombre = forms.CharField(max_length=40)
	p_apellido = forms.CharField(max_length=40)
	s_apellido = forms.CharField(max_length=40)
	fecha = forms.CharField(max_length=10)
	telefono = forms.CharField(max_length=40)
	esta_civi = (
		("Casado", "Casado"),
		("Soltero", "Soltero"),
		("Viudo", "Viudo"),
		("Divorciado", "Divorciado"),
	)
	esta_civil = forms.ChoiceField(choices=esta_civi)
	nivel = (
		("Primaria", "Primaria"),
		("Secundaria", "Secundaria"),
		("Bachiller", "Bachiller"),
		("Universitario", "Universitario"),
		)
	nivel_instruc = forms.ChoiceField(choices=nivel)
	profesion = models.CharField(max_length=50)
	email = forms.EmailField(max_length=254)
	generos = (
		("Femenino","Femenino"),
		("Masculino","Masculino"),
	)
	genero = forms.ChoiceField(choices=generos)
	trabaja1 = (
		("Si","Si"),
		("No", "No"),
		)
	trabaja = forms.ChoiceField(choices=trabaja1)
	inscrito1 = (
		("Si","Si"),
		("No","No"),
	)
	inscrito = forms.ChoiceField(choices=inscrito1)
	posee_registro = (
		("G.M.V.V", "G.M.V.V"),
		("0800 Mi Hogar", "0800 Mi Hogar"),
	)
	registro = forms.ChoiceField(choices=posee_registro)
	pare = (
		("Si", "No"),
		("No", "No"),
	)
	pareja = forms.ChoiceField(choices=pare)
	ingre_mensual = forms.CharField(max_length=20)
	direccion = forms.CharField(max_length=400)
	User._meta.get_field('email')._unique = True

	class Meta:
		model = User
		User._meta.get_field('email')._unique = True
		User._meta.get_field('username')._unique = True
		fields = ('username', 'p_nombre', 's_nombre', 'p_apellido', 's_apellido', 'telefono', 'email', 'genero', 'direccion', 'password1', 'password2', )

class EditarPUserForm(forms.ModelForm):
	class Meta:
		model = PUser
		fields= (
			'p_nombre',
			's_nombre',
			'p_apellido',
			's_apellido',
			'telefono',
			'genero',
			'cargo',
			'direccion'
		)

	def __init__(self, *args, **kwargs):
		super(EditarPUserForm, self).__init__(*args, **kwargs)
		f = self.fields.get('user_permissions', None)
		if f is not None:
			f.queryset = f.queryset.select_related('content_type')

class EditarUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('email',)

	def __init__(self, *args, **kwargs):
		super(EditarUserForm, self).__init__(*args, **kwargs)
		f = self.fields.get('user_permissions', None)
		if f is not None:
			f.queryset = f.queryset.select_related('content_type')