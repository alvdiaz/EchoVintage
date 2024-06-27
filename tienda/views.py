from django.shortcuts import render, redirect, get_object_or_404
from .models import Vinilo, Cassette, Cd
from .forms import ViniloForm, CassetteForm, CdForm, CustomUserCreationForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def home(request):
    return render(request,'tienda/home.html')

def cassetes(request):
    cassettes = Cassette.objects.all()
    data = {
    'cassettes': cassettes
    }
    return render(request,'tienda/cassetes.html', data)

def carrito(request):
    return render(request,'tienda/carrito.html')

def cds(request):
    cds = Cd.objects.all()
    data = {
        'cds': cds
    }
    return render(request,'tienda/cds.html', data)

def contacto(request):
    return render(request,'tienda/contacto.html')

def vinilos(request):
    vinilos = Vinilo.objects.all()
    data = {
        'vinilos': vinilos
    }
    return render(request,'tienda/vinilos.html', data)

def agregarvinilo(request):
    data = {
        'form':ViniloForm()
    }

    if request.method == "POST":
        formulario = ViniloForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'tienda/vinilos/agregar.html', data)

def agregarcassette(request):
    data = {
        'form':CassetteForm()
    }

    if request.method == "POST":
        formulario = CassetteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'tienda/vinilos/agregar_cassette.html', data)

def agregarcd(request):
    data = {
        'form':CdForm()
    }

    if request.method == "POST":
        formulario = CdForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'tienda/vinilos/agregar_cd.html', data)

def listar_productos(request):
    vinilos= Vinilo.objects.all()
    cassettes= Cassette.objects.all()
    cds= Cd.objects.all()
    data={
        'vinilos':vinilos,
        'cassettes':cassettes,
        'cds':cds
    }
    return render(request, 'tienda/vinilos/listar.html', data)


def modificar_producto(request, tipo, id):
    if tipo == "vinilo":
        producto = get_object_or_404(Vinilo, id=id)
        form_class = ViniloForm
    elif tipo == "cassette":
        producto = get_object_or_404(Cassette, id=id)
        form_class = CassetteForm
    elif tipo == "cd":
        producto = get_object_or_404(Cd, id=id)
        form_class = CdForm
    else:
        raise Http404("Producto no encontrado")

    data = {
        'form': form_class(instance=producto),
        'tipo': tipo
    }
    if request.method == 'POST':
        formulario = form_class(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado con Exito")
            return redirect(to="listar_productos")
        data["form"] = formulario

    return render(request, 'tienda/vinilos/modificar.html', data)

def eliminar_producto(request, tipo, id):
    if tipo == "vinilo":
        producto = get_object_or_404(Vinilo, id=id)
    elif tipo == "cassette":
        producto = get_object_or_404(Cassette, id=id)
    elif tipo == "cd":
        producto = get_object_or_404(Cd, id=id)
    else:
        raise Http404("Producto no encontrado")

    if request.method == "POST":
        producto.delete()
        messages.success(request, "Eliminado con exito")
        return redirect(to="listar_productos")

    return redirect(to="listar_productos")

def es_superuser(user):
    return user.is_superuser

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    data={
        'form':CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario= CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"]= formulario
    return render(request, 'registration/registro.html', data)