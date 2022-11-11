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


class Pacientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    telefono = models.IntegerField()
    id_os = models.ForeignKey(ObrasSociales, null=True, blank=True, verbose_name="Obra Social", on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.nombre} {self.apellido} \nDNI: {self.dni} \nObras social: {self.id_os}'
    
    class Meta:
        verbose_name='Paciente'
