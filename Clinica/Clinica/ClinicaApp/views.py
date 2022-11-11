from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ObrasSociales, Especialidades, Pacientes, Consultorios, Horarios
from .forms import OSFormulario, EspecialidadesFormulario

def inicio(request):
    return render(request, "inicio.html")

class OSCreate(CreateView):
    model = ObrasSociales
    template_name = "os/os_create.html"
    fields = ["descripcion"]
    success_url = "/clinica-app/"

class OSList(ListView):
    model = ObrasSociales
    template_name = "os/os_list.html"
    context_object_name = "obras_sociales"

class OSDetail(DetailView):
    model = ObrasSociales
    template_name = "os/os_detail.html"
    context_object_name = "obra_social"

class OSUpdate(UpdateView):
    model = ObrasSociales
    template_name = "os/os_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class OSDelete(DeleteView):
    model = ObrasSociales
    template_name = "os/os_delete.html"
    success_url = "/clinica-app/"

def busquedaOS(request):
    return render(request, 'buscar_os.html')

def buscarOS(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.GET['descripcion']:
        descripcion = request.GET['descripcion']
        obras_sociales = ObrasSociales.objects.filter(descripcion__icontains=descripcion)
        return render(request, "resultado_os.html", {"obras_sociales":obras_sociales, "descripcion":descripcion})
    else:
        return render(request, "inicio.html")

class EspecialidadCreate(CreateView):
    model = Especialidades
    template_name = "especialidad_create.html"
    fields = ["descripcion"]
    success_url = "/clinica-app/"

class EspecialidadList(ListView):
    model = Especialidades
    template_name = "especialidad_list.html"
    context_object_name = "especialidades"

class EspecialidadUpdate(UpdateView):
    model = Especialidades
    template_name = "especialidad_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class EspecialidadDelete(DeleteView):
    model = Especialidades
    template_name = "especialidad_delete.html"
    success_url = "/clinica-app/"

class PacienteCreate(CreateView):
    model = Pacientes
    template_name = "pacientes_create.html"
    fields = ["nombre","apellido","dni","telefono","id_os"]
    success_url = "/clinica-app/"

class PacienteDetail(DetailView):
    model = Pacientes
    template_name = "paciente_detail.html"
    context_object_name = "paciente"

class PacienteUpdate(UpdateView):
    model = Pacientes
    template_name = "paciente_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class PacientedDelete(DeleteView):
    model = Pacientes
    template_name = "paciente_delete.html"
    success_url = "/clinica-app/"

class ConsultorioCreate(CreateView):
    model = Consultorios
    template_name = "consultorios_create.html"
    fields = ["nro_direccion", "consultorio"]
    success_url = "/clinica-app/"

class ConsultorioUpdate(UpdateView):
    model = Consultorios
    template_name = "consultorio_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class ConsultorioDetail(DetailView):
    model = Consultorios
    template_name = "consultorio_detail.html"
    context_object_name = "consultorio"

class HorarioCreate(CreateView):
    model = Horarios
    template_name = "horarios_create.html"
    fields = ["hora"]
    success_url = "/clinica-app/"
