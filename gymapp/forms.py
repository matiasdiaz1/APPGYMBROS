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
            'peso': forms.NumberInput(attrs={'step': '0.1'}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super(MancuernaForm, self).__init__(*args, **kwargs)
        self.fields['peso'].label = "Peso de la mancuerna"
        self.fields['peso'].help_text = "Seleccione el peso de la mancuerna"
        

class CustomUserCreationForm(UserCreationForm):
    pass