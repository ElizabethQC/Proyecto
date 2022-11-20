from django import forms
from models import Pacientes, Doctores

class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    id_os = forms.CharField(max_length=20)

class OSFormulario(forms.Form):
    descripcion = forms.CharField(max_length=20)

class EspecialidadesFormulario(forms.Form):
    descripcion = forms.CharField(max_length=20)

class ConsultoriosFormulario(forms.Form):
    nro_consultorio = forms.IntegerField()
    direccion = forms.CharField(max_length=20)

class PacienteRegisterForm(UserCreationForm):
    nombre =forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Pacientes
        fields = ["nombre", "apellido", "dni", "telefono", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class DoctorRegisterForm(UserCreationForm):
    nombre =forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Doctores
        fields = ["nombre", "apellido", "dni", "telefono", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}