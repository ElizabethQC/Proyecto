from django import forms
from django.db import models
from .models import Pacientes, Doctores, ObrasSociales
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    id_os = forms.IntegerField()

class OSFormulario(forms.Form):
    descripcion = forms.CharField(max_length=20)

class EspecialidadesFormulario(forms.Form):
    descripcion = forms.CharField(max_length=20)

class ConsultoriosFormulario(forms.Form):
    nro_consultorio = forms.IntegerField()
    direccion = forms.CharField(max_length=20)

class PacienteRegisterForm(UserCreationForm):

   class Meta:
        model =  User
        fields = ['username', 'last_name', 'first_name', 'email']
        help_texts = {k:"" for k in fields}

class DoctorRegisterForm(UserCreationForm):

    class Meta:
        model =  User
        fields = ['username', 'last_name', 'first_name', 'email']
        help_texts = {k:"" for k in fields}
        
