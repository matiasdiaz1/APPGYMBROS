from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona, Mancuerna
from .forms import PersonaForm, UpdatePersonaForm

# Create your views here.

def index(request):
    return render(request, 'gymapp/index.html')


def personas(request):
    people = Persona.objects.all()  # queryset
    datos = {
        "personas": people
    }
    return render(request, 'gymapp/personas.html', datos)

def crearpersona(request):
    form = PersonaForm()
    if request.method == "POST":
        form = PersonaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="personas")
    datos = {
        "form": form
    }
    return render(request, 'gymapp/crearpersona.html', datos)

def detallepersona(request, id):
    persona = get_object_or_404(Persona, rut=id)
    mancuernas = Mancuerna.objects.filter(propietario=persona)  # Obtener mancuernas de la persona
    datos = {
        "persona": persona,
        "mancuernas": mancuernas  # Agregar mancuernas al contexto
    }
    return render(request, 'gymapp/detallepersona.html', datos)

def modificar(request, id):
    persona = get_object_or_404(Persona, rut=id)
    form = UpdatePersonaForm(instance=persona)
    if request.method == "POST":
        form = UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            return redirect(to="personas")
    datos = {
        "form": form,
        "persona": persona
    }
    return render(request, 'gymapp/modificar.html', datos)

def eliminar(request, id):
    persona = get_object_or_404(Persona, rut=id)
    if request.method == "POST":
        persona.delete()
        return redirect(to="personas")
    datos = {
        "persona": persona
    }
    return render(request, 'gymapp/eliminar.html', datos)