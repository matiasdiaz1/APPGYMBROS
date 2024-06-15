

from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

TIPO_SEXO = (
    ("F", "FEMENINO"),
    ("M", "MASCULINO"),
    ("O", "OTRO")
)

TIPO_MANCUERNA = (
    ("10", "10 kilos"),
    ("20", "20 kilos"),
)

class Persona(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fnacto = models.DateField(default=date.today)
    correo = models.EmailField(verbose_name='E-mail')
    sexo = models.CharField(max_length=1, choices=TIPO_SEXO)
    foto = models.ImageField(upload_to='personas', null=True)

    def __str__(self):
        return f"{self.rut} -  {self.nombre} {self.apellido}"

class Mancuerna(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    tipo = models.CharField(max_length=2, null=False, choices=TIPO_MANCUERNA)
    propietario = models.ForeignKey(Persona, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nombre} ({self.tipo} kilos)"