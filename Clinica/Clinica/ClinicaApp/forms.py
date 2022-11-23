from django import forms
from django.db import models
from .models import Pacientes, Doctores, ObrasSociales
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class PacientesFormulario(forms.Form):
#     nombre = forms.CharField(max_length=20)
#     apellido = forms.CharField(max_length=20)
#     dni = forms.IntegerField()
#     telefono = forms.IntegerField()
#     id_os = forms.CharField(max_length=20)

class OSFormulario(forms.Form):
    descripcion = forms.CharField(max_length=20)

class EspecialidadesFormulario(forms.Form):
    descripcion = forms.CharField(max_length=20)

class ConsultoriosFormulario(forms.Form):
    nro_consultorio = forms.IntegerField()
    direccion = forms.CharField(max_length=20)

class PacienteRegisterForm(UserCreationForm):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    id_os = forms.CharField(label="Obras social", max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model =  User
        fields = ["username", "nombre", "apellido", "dni", "telefono", "id_os", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
    
    class Os:
        model = ObrasSociales
        fields = ["id_os"]

class DoctoresRegisterForm(UserCreationForm):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model =  User
        fields = ["username", "nombre", "apellido", "dni", "telefono", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
