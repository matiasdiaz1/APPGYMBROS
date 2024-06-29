from datetime import date
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

TIPO_SEXO = (
    ("F", "FEMENINO"),
    ("M", "MASCULINO"),
    ("O", "OTRO")
)

PESO_CHOICES = (
    (10, "10 kg"),
    (20, "20 kg"),
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
    id = models.AutoField(primary_key=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.1)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    propietario = models.ForeignKey(Persona, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Mancuerna de {self.peso} kg"

    def __str__(self):
        return f"Mancuerna de {self.peso} kg - ${self.precio}"