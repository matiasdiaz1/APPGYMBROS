from django import forms
from .models import Persona
from .models import Mancuerna

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
        fields = ['peso']
        widgets = {
            'peso': forms.Select(choices=[(10, '10 kg'), (20, '20 kg')])
        }

    def __init__(self, *args, **kwargs):
        super(MancuernaForm, self).__init__(*args, **kwargs)
        self.fields['peso'].label = "Peso de la mancuerna"
        self.fields['peso'].help_text = "Seleccione el peso de la mancuerna"