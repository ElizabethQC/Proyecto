from django.contrib import admin

from .models import ObrasSociales, Especialidades, Pacientes, Consultorios

admin.site.register(ObrasSociales)
admin.site.register(Especialidades)
admin.site.register(Pacientes)
admin.site.register(Consultorios)
