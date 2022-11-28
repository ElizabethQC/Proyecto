from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ObrasSociales, Especialidades, Pacientes, Consultorios, Horarios, Doctores, Persona
from .forms import OSFormulario, EspecialidadesFormulario, PacienteRegisterForm, DoctorRegisterForm

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
    return render(request, 'os/buscar_os.html')

def buscarOS(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.GET['descripcion']:
        descripcion = request.GET['descripcion']
        obras_sociales = ObrasSociales.objects.filter(descripcion__icontains=descripcion)
        return render(request, "os/resultado_os.html", {"obras_sociales":obras_sociales, "descripcion":descripcion})
    else:
        return render(request, "inicio.html")

class EspecialidadCreate(CreateView):
    model = Especialidades
    template_name = "especialidades/especialidad_create.html"
    fields = ["descripcion"]
    success_url = "/clinica-app/"

class EspecialidadList(ListView):
    model = Especialidades
    template_name = "especialidades/especialidad_list.html"
    context_object_name = "especialidades"

class EspecialidadUpdate(UpdateView):
    model = Especialidades
    template_name = "especialidades/especialidad_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class EspecialidadDelete(DeleteView):
    model = Especialidades
    template_name = "especialidades/especialidad_delete.html"
    success_url = "/clinica-app/"

class PacienteCreate(CreateView):
    model = Pacientes
    template_name = "pacientes/paciente_create.html"
    fields = ["nombre","apellido","dni","telefono","id_os"]
    success_url = "/clinica-app/"

class PacienteDetail(DetailView):
    model = Pacientes
    template_name = "pacientes/paciente_detail.html"
    context_object_name = "paciente"

class PacienteList(ListView):
    model = Pacientes
    template_name = "pacientes/paciente_list.html"
    context_object_name = "pacientes"

class PacienteUpdate(UpdateView):
    model = Pacientes
    template_name = "pacientes/paciente_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class PacienteDelete(DeleteView):
    model = Pacientes
    template_name = "pacientes/paciente_delete.html"
    success_url = "/clinica-app/"

class ConsultorioCreate(CreateView):
    model = Consultorios
    template_name = "consultorios/consultorio_create.html"
    fields = ["nro_direccion", "consultorio"]
    success_url = "/clinica-app/"

class ConsultorioList(ListView):
    model = Consultorios
    template_name = "consultorios/consultorio_list.html"
    context_object_name = "consultorios"

class ConsultorioUpdate(UpdateView):
    model = Consultorios
    template_name = "consultorios/consultorio_update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"

class ConsultorioDetail(DetailView):
    model = Consultorios
    template_name = "consultorios/consultorio_detail.html"
    context_object_name = "consultorio"

class ConsultorioDelete(DeleteView):
    model = Consultorios
    template_name = "consultorios/consultorio_delete.html"
    success_url = "/clinica-app/"

class HorarioCreate(CreateView):
    model = Horarios
    template_name = "horarios/horario_create.html"
    fields = ["hora"]
    success_url = "/clinica-app/"

class HorarioList(ListView):
    model = Horarios
    template_name = "horarios/horario_list.html"
    context_object_name = "horarios"

class HorarioUpdate(UpdateView):
    model = Horarios
    template_name = "horarios/horario__update.html"
    fields = ('__all__')
    success_url = "/clinica-app/"
    
class HorarioDelete(DeleteView):
    model = Horarios
    template_name = "horarios/horario_delete.html"
    success_url = "/clinica-app/"    

class DoctorList(ListView):
    model = Doctores
    template_name = "doctores/doctor_list.html"
    context_object_name = "doctores"

class DoctorDelete(DeleteView):
    model = Doctores
    template_name = "doctores/doctor_delete.html"
    success_url = "/clinica-app/"    

def registrarPaciente(request):
      if request.method == 'POST':
            form = PacienteRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data["username"]
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario creado"})
      else:
            form = PacienteRegisterForm()            
      return render(request,"registro_paciente.html" ,  {"form":form})

def registrarDoctor(request):
      if request.method == 'POST':
            form = DoctorRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data["username"]
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario creado"})
      else:
            form = DoctorRegisterForm()            
      return render(request,"registro_doctor.html" ,  {"form":form})

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "inicio.html", {"mensaje":f"Bienvenido"})
            else:
                return render(request, "inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "inicio.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})

@login_required
def obras_sociales(request):

    lista = ObrasSociales.objects.all() 

    return render(request, "os_list.html", {"obras_sociales": lista})

@staff_member_required(login_url="/clinica-app/login")

def pacientes(request):
    return render(request, "pacientes_list.html")

def doctores(request):
    return render(request, "doctores_list.html")
