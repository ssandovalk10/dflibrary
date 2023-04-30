from django.db import models


class Departamento(models.Model):
    departamento = models.CharField('Departamento', max_length=60)

    def __str__(self):
        return str(self.id) + '-' + self.departamento
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO')

    )

    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=50)
    job = models.CharField('Trabajo', max_length=50)
    avatar = models.ImageField(upload_to ='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,blank=True, null=True)

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la empresa'
        

    def __str__(self):
        return str(self.id) + '-' + self.first_name