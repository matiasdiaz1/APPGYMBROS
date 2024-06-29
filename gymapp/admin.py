from django.contrib import admin
from .models import Persona, Mancuerna

class AdmPersona(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'foto', 'fnacto', 'correo', 'sexo']
    list_filter = ['sexo']

class AdmMancuerna(admin.ModelAdmin):
    list_display = ['id', 'peso', 'precio', 'propietario']
    list_filter = ['peso']
    search_fields = ['propietario__nombre', 'propietario__apellido']

admin.site.register(Persona, AdmPersona)
admin.site.register(Mancuerna, AdmMancuerna)