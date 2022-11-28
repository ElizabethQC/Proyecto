from django.contrib import admin

from .models import ObrasSociales, Especialidades, Pacientes, Consultorios, Doctores, Persona, Horarios

admin.site.register(ObrasSociales)
admin.site.register(Especialidades)
admin.site.register(Pacientes)
admin.site.register(Consultorios)
admin.site.register(Horarios)
admin.site.register(Doctores)
admin.site.register(Persona)
