from django import forms

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