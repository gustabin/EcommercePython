from django.shortcuts import render, redirect
from .models import Categorias
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    categoriasListado = Categorias.objects.all()
    messages.success(request, '¡Categorias listadas!')
    return render(request, "gestionCategorias.html", {"categorias": categoriasListado})

def registrarCategoria(request):
    nombre= request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    idEmpresa = request.POST['txtIdEmpresa']
    fecha = datetime.now()

    categoria = Categorias.objects.create(nombre=nombre, descripcion=descripcion, idEmpresa=idEmpresa, fecha=fecha)
    messages.success(request, '¡Categoria guardada!')
    return redirect('/')

def edicionCategoria(request, id):
    categoria = Categorias.objects.get(id=id)
    return render(request, "edicionCategoria.html", {"categoria": categoria})

def editarCategoria(request):
    id= request.POST['txtId']
    nombre= request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    idEmpresa = request.POST['txtIdEmpresa']

    categoria = Categorias.objects.get(id=id)
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    categoria.idEmpresa = idEmpresa
    categoria.save()
    messages.success(request, '¡Categoria actualizada!')
    return redirect('/')

def eliminacionCategoria(request, id):
    categoria = Categorias.objects.get(id=id)
    categoria.delete()
    messages.success(request, '¡Categoria eliminada!')
    return redirect('/')
