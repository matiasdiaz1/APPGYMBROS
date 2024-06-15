from django import forms
from .models import Persona

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

