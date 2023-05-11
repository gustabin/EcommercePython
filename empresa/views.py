from django.shortcuts import render, redirect
from .models import Empresa
# from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    empresaListado = Empresa.objects.all()
    messages.success(request, 'Empresas listadas!')
    return render(request, "gestionEmpresa.html", {"empresas": empresaListado})

def registrarEmpresa(request):
    nombre= request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    ciudad = request.POST['txtCiudad']
    # fecha = datetime.now()
    empresa = Empresa.objects.create(nombre=nombre, telefono=telefono, ciudad=ciudad)
    messages.success(request, '¡Empresa guardada!')
    return redirect('/empresa/')

def edicionEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    return render(request, "edicionEmpresa.html", {"empresa": empresa})

def editarEmpresa(request):
    id= request.POST['txtId']
    nombre= request.POST['txtNombre']
    telefono = request.POST['txtTelefono']
    ciudad = request.POST['txtCiudad']

    empresa = Empresa.objects.get(id=id)
    empresa.nombre = nombre
    empresa.telefono = telefono
    empresa.ciudad = ciudad
    empresa.save()
    messages.success(request, '¡Empresa actualizada!')
    return redirect('/empresa/')

def eliminacionEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.success(request, 'Empresa eliminada!')
    return redirect('/empresa/')