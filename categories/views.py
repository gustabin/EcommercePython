from django.shortcuts import render, redirect
from .models import Categorias
from empresa.models import Empresa
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

    # ojo cambiar esto que es provisional
    request.session['empresa_id'] = 26
    empresa_id = request.session.get('empresa_id', None)
    if empresa_id is not None:
        empresa = Empresa.objects.get(id=empresa_id)
    else:
        return redirect('login')

    fecha = datetime.now()
    imagen    = request.FILES.get('txtImagen',    'categoria/sinImagen.png') 

    categoria = Categorias.objects.create(nombre=nombre, descripcion=descripcion, empresa_id=empresa, fecha=fecha, imagen=imagen)
    messages.success(request, '¡Categoria guardada!')
    return redirect('/')

def edicionCategoria(request, id):
    categoria = Categorias.objects.get(id=id)
    return render(request, "edicionCategoria.html", {"categoria": categoria})

def editarCategoria(request):
    id= request.POST['txtId']
    nombre= request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    # empresa_id = request.POST['txtEmpresa_id'] 


    categoria = Categorias.objects.get(id=id)
    categoria.nombre = nombre
    categoria.descripcion = descripcion
    # categoria.empresa_id = empresa_id
    
    if 'txtImagen' in request.FILES:
        imagen = request.FILES['txtImagen']
        categoria.imagen = imagen
    categoria.save()
    messages.success(request, '¡Categoria actualizada!')
    return redirect('/')

def eliminacionCategoria(request, id):
    categoria = Categorias.objects.get(id=id)
    categoria.delete()
    messages.success(request, '¡Categoria eliminada!')
    return redirect('/')
