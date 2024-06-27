from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona
from .forms import PersonaForm, UpdatePersonaForm
from .models import Mancuerna
from .forms import MancuernaForm
import os

# Create your views here.

def index(request):
    return render(request, 'gymapp/index.html')


def personas(request):
    people = Persona.objects.all()  
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
    mancuernas = Mancuerna.objects.filter(propietario=persona)  
    datos = {
        "persona": persona,
        "mancuernas": mancuernas  
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

        if persona.foto:
            if os.path.isfile(persona.foto.path):
                os.remove(persona.foto.path)

        persona.delete()
        return redirect(to="personas")
    datos = {
        "persona": persona
    }
    return render(request, 'gymapp/eliminar.html', datos)

def lista_mancuernas(request):
    mancuernas = Mancuerna.objects.all()
    return render(request, 'gymapp/lista_mancuernas.html', {'mancuernas': mancuernas})

def crear_mancuerna(request):
    if request.method == 'POST':
        form = MancuernaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mancuernas')
    else:
        form = MancuernaForm()
    return render(request, 'gymapp/crear_mancuerna.html', {'form': form})

def asignar_mancuerna(request, id):
    mancuerna = get_object_or_404(Mancuerna, id=id)
    if request.method == 'POST':
        persona_id = request.POST.get('persona')
        persona = get_object_or_404(Persona, rut=persona_id)
        mancuerna.propietario = persona
        mancuerna.save()
        return redirect('lista_mancuernas')
    personas = Persona.objects.all()
    return render(request, 'gymapp/asignar_mancuerna.html', {'mancuerna': mancuerna, 'personas': personas})