from django.db import models

class ObrasSociales(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.descripcion}'

class Especialidades(models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.descripcion}'

class Consultorios(models.Model):
    nro_consultorio = models.IntegerField()
    direccion = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.direccion} n\Consultorio: {self.nro_consultorio}'

class Horarios(models.Model):
    hora = models.TimeField()

class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

class Pacientes(Persona):
    id_os = models.ForeignKey(ObrasSociales, null=True, blank=True, verbose_name="Obra Social", on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - DNI: {self.dni} - Obra social: {self.id_os}'
    
    class Meta:
        verbose_name='Paciente'

class Doctores(Persona):
    id_especialidad = models.ForeignKey(Especialidades, null=True, blank=True, verbose_name="Especialidad", on_delete=models.RESTRICT)
    # id_consultorio = models.ForeignKey(Consultorios, null=True, blank=True, verbose_name="Consultorio", on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - Especialidad: {self.id_especialidad}'
    
