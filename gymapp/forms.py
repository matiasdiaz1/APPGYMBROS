from django import forms
from .models import Persona
from .models import Mancuerna
from django.contrib.auth.forms import UserCreationForm

class PersonaForm(forms.ModelForm):
    rut = forms.CharField(help_text="Ingrese rut sin puntos y con guión")
    fnacto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")

    class Meta:
        model = Persona
        fields = ['rut', 'nombre', 'apellido', 'foto', 'fnacto', 'correo', 'sexo']

class UpdatePersonaForm(forms.ModelForm):
    fnacto = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'foto', 'fnacto', 'correo', 'sexo']

class MancuernaForm(forms.ModelForm):
    class Meta:
        model = Mancuerna
        fields = ['peso', 'precio', 'propietario']
        widgets = {
            'peso': forms.NumberInput(attrs={'step': '1'}),  # Ajustado para enteros
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(MancuernaForm, self).__init__(*args, **kwargs)
        self.fields['peso'].label = "Peso de la mancuerna"
        self.fields['peso'].help_text = "Seleccione el peso de la mancuerna"


class CustomUserCreationForm(UserCreationForm):
    pass

class DireccionForm(forms.Form):
    direccion = forms.CharField(label='Dirección', max_length=100)
    numero = forms.CharField(label='Número', max_length=10)
    depto = forms.CharField(label='Depto/Casa/Oficina', max_length=50, required=False)
    celular = forms.CharField(label='Celular', max_length=15)
    region = forms.ChoiceField(label='Región', choices=[('Region 1', 'Region 1'), ('Region 2', 'Region 2')])  # Añade tus regiones
    comuna = forms.ChoiceField(label='Comuna', choices=[('Comuna 1', 'Comuna 1'), ('Comuna 2', 'Comuna 2')])  # Añade tus comunas
    instrucciones = forms.CharField(label='Instrucciones de entrega', widget=forms.Textarea, required=False)
    nombre_direccion = forms.CharField(label='Nombre de la dirección', max_length=100)
    
class PagoForm(forms.Form):
    numero_tarjeta = forms.CharField(max_length=16, label='Número de tarjeta', widget=forms.TextInput(attrs={'placeholder': 'Número de tarjeta'}))
    mes_vencimiento = forms.ChoiceField(choices=[(str(i).zfill(2), str(i).zfill(2)) for i in range(1, 13)], label='Mes de vencimiento')
    ano_vencimiento = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(2024, 2035)], label='Año de vencimiento')
    cvv = forms.CharField(max_length=3, label='CVV', widget=forms.TextInput(attrs={'placeholder': 'CVV'}))
    rut_dueno_tarjeta = forms.CharField(max_length=12, label='RUT dueño de tarjeta', widget=forms.TextInput(attrs={'placeholder': 'RUT dueño de tarjeta'}))