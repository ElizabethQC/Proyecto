from django.urls import path
from .views import inicio, OSCreate, OSList, OSUpdate, OSDetail, OSDelete, buscarOS, busquedaOS, EspecialidadCreate, EspecialidadList, EspecialidadUpdate, EspecialidadDelete, PacienteCreate, PacienteDelete, PacienteDetail, PacienteList, PacienteUpdate, ConsultorioCreate, ConsultorioDetail, ConsultorioUpdate

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('agregar-os/', OSCreate.as_view(), name="AgregarOS"),
    path('listado-os/', OSList.as_view(), name="ListadoOS"),
    path('editar-os/<pk>', OSUpdate.as_view(), name="EditarOS"),
    path('detalle-os/<pk>', OSDetail.as_view(), name="DetalleOS"),
    path('elimiar-os/<pk>', OSDelete.as_view(), name="EliminarOS"),
    path('buscar-os/', busquedaOS, name="BuscarOS"),
    path('resultado-os/', buscarOS, name="ResultadoOS"),
    path('agregar-especialidad/', EspecialidadCreate.as_view(), name="AgregarEspecialidad"),
    path('listado-especialidad/', EspecialidadList.as_view(), name="ListadoEspecialidad"),
    path('editar-especialidad/<pk>', EspecialidadUpdate.as_view(), name="EditarEspecialidad"),
    path('eliminar-especialidad/<pk>', EspecialidadDelete.as_view(), name="EliminarEspecialidad"),
    path('agregar-paciente/', PacienteCreate.as_view(), name="AgregarPaciente"),
    path('listado-pacientes/', PacienteList.as_view(), name="ListadoPaciente"),
    path('editar-paciente/<pk>', PacienteUpdate.as_view(), name="EditarPaciente"),
    path('detalle-paciente/<pk>', PacienteDetail.as_view(), name="DetallePaciente"),
    path('eliminar-paciente/<pk>', PacienteDelete.as_view(), name="EliminarPaciente"),
    path('agregar-consultorio/', ConsultorioCreate.as_view(), name="AgregarConsultorio")
]
