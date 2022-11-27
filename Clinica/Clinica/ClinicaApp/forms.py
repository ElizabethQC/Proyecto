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
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    def __init__(self,**kwargs):
        id_os = kwargs.get('id_os', )
        super(PacienteRegisterForm, self).__init__(**kwargs)
        self.fields['id_os']=forms.ModelChoiceField(label="Obra social", queryset=ObrasSociales.objects.all())

    class Meta:
        model =  User
        fields = ["username", "nombre", "apellido", "dni", "telefono", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
    

class DoctorRegisterForm(UserCreationForm):
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
