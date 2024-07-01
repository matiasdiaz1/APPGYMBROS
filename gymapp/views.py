from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona, Mancuerna
from .forms import PagoForm, CustomUserCreationForm, PersonaForm, UpdatePersonaForm, MancuernaForm , DireccionForm
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from .cart import Cart
import os
from django.contrib import messages

def index(request):
    mancuernas = Mancuerna.objects.all()[:6]  
    return render(request, 'gymapp/index.html', {'mancuernas': mancuernas})

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
            messages.success(request, 'La persona ha sido agregada exitosamente.')
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
            messages.warning(request, 'La persona ha sido modificada exitosamente.')
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
        messages.error(request, 'La persona ha sido eliminada exitosamente.')
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

def registro(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"] )
            login (request, user)
            return redirect(to="index")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data )

@require_POST
def cart_add(request, mancuerna_id):
    cart = Cart(request)
    mancuerna = get_object_or_404(Mancuerna, id=mancuerna_id)
    quantity = int(request.POST.get('quantity'))
    cart.add(mancuerna=mancuerna, quantity=quantity, update_quantity=True)
    return redirect('cart_detail')

def cart_remove(request, mancuerna_id):
    cart = Cart(request)
    mancuerna = get_object_or_404(Mancuerna, id=mancuerna_id)
    cart.remove(mancuerna)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'gymapp/cart_detail.html', {'cart': cart})


def direccion_entrega(request):
    if request.method == "POST":
        form = DireccionForm(request.POST)
        if form.is_valid():
            return redirect('pago')  
    else:
        form = DireccionForm()
    return render(request, 'gymapp/direccion_entrega.html', {'form': form})

def pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            return redirect('confirmacion')  
    else:
        form = PagoForm()
    return render(request, 'gymapp/pago.html', {'form': form})



def monedas(request):
    return render(request, 'gymapp/monedas.html')