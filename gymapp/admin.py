from django.contrib import admin
from .models import Persona, Mancuerna

class AdmPersona(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'foto', 'fnacto', 'correo', 'sexo']
    list_filter = ['sexo']

class AdmMancuerna(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'tipo', 'propietario']
    list_filter = ['propietario', 'tipo']

admin.site.register(Persona, AdmPersona)
admin.site.register(Mancuerna, AdmMancuerna)