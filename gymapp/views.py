from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona, Mancuerna
from .forms import PagoForm, CustomUserCreationForm, PersonaForm, UpdatePersonaForm, MancuernaForm , DireccionForm
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_POST
from .cart import Cart
import os
from django.contrib import messages
from django.contrib.auth.decorators import login_required , user_passes_test

def es_admin(usuario):
    if not usuario.is_staff:
        messages.error(usuario.request, "No tienes permiso para acceder a esta página.")
        return False
    return True


def index(request):
    mancuernas = Mancuerna.objects.all()[:6]  
    return render(request, 'gymapp/index.html', {'mancuernas': mancuernas})

@login_required
def personas(request):
    people = Persona.objects.all()  
    datos = {
        "personas": people
    }
    return render(request, 'gymapp/personas.html', datos)

@login_required
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

@login_required
def detallepersona(request, id):
    persona = get_object_or_404(Persona, rut=id)
    mancuernas = Mancuerna.objects.filter(propietario=persona)  
    datos = {
        "persona": persona,
        "mancuernas": mancuernas  
    }
    return render(request, 'gymapp/detallepersona.html', datos)

@login_required
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

@login_required
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

@login_required
def lista_mancuernas(request):
    mancuernas = Mancuerna.objects.all()
    return render(request, 'gymapp/lista_mancuernas.html', {'mancuernas': mancuernas})

@login_required
def crear_mancuerna(request):
    if request.method == 'POST':
        form = MancuernaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mancuernas')
    else:
        form = MancuernaForm()
    return render(request, 'gymapp/crear_mancuerna.html', {'form': form})

@login_required
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
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > mancuerna.stock:
        messages.error(request, f"Lo sentimos, solo hay {mancuerna.stock} unidades disponibles.")
        return redirect('cart_detail')
    
    cart.add(mancuerna=mancuerna, quantity=quantity, update_quantity=True)
    return redirect('cart_detail')
@login_required
def cart_remove(request, mancuerna_id):
    cart = Cart(request)
    mancuerna = get_object_or_404(Mancuerna, id=mancuerna_id)
    cart.remove(mancuerna)
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'gymapp/cart_detail.html', {'cart': cart})


@login_required
def direccion_entrega(request):
    if request.method == "POST":
        form = DireccionForm(request.POST)
        if form.is_valid():
            request.session['direccion'] = form.cleaned_data
            return redirect('pago')
    else:
        initial_data = {
            'nombre': request.user.first_name + ' ' + request.user.last_name,
            'email': request.user.email,
        }
        form = DireccionForm(initial=initial_data)
    return render(request, 'gymapp/direccion_entrega.html', {'form': form})

@login_required
def pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            return redirect('confirmacion')
    else:
        form = PagoForm()
    return render(request, 'gymapp/pago.html', {'form': form})


@login_required
def confirmacion(request):
    cart = Cart(request)
    direccion = request.session.get('direccion', {})
    usuario = request.user  
    return render(request, 'gymapp/confirmacion.html', {'cart': cart, 'direccion': direccion, 'usuario': usuario})

@login_required
def monedas(request):
    return render(request, 'gymapp/monedas.html')


@login_required
def confirmacion(request):
    cart = Cart(request)
    direccion = request.session.get('direccion', {})
    usuario = request.user


    for item in cart:
        mancuerna = item['mancuerna']
        if mancuerna.stock < item['quantity']:
            messages.error(request, f"Lo sentimos, no hay suficiente stock para {mancuerna}.")
            return redirect('cart_detail')
        mancuerna.stock -= item['quantity']
        mancuerna.save()


    cart.clear()
    
    return render(request, 'gymapp/confirmacion.html', {'cart': cart, 'direccion': direccion, 'usuario': usuario})



@login_required
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    messages.info(request, 'El carrito ha sido vaciado exitosamente.')
    return redirect('cart_detail')



@user_passes_test(es_admin, login_url='index')
def confirmacion_admin(request):
    return render(request, 'gymapp/confirmacion_admin.html')