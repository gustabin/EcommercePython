from django.shortcuts import render, redirect
from .models import Marca
from empresa.models import Empresa
from datetime import datetime
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from django.core.files.storage import FileSystemStorage

def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(file.name, file)
        return render(request, 'upload.html', {'file_url': fs.url(file.name)})
    return render(request, 'upload.html')

def home(request):
    marcaListado = Marca.objects.all()
    messages.success(request, 'Marcas listadas!')
    return render(request, "gestionMarca.html", {"marcas": marcaListado})

def registrarMarca(request):

    print(request.POST)
    nombre= request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    mostrarMarcas = request.POST['txtMostrarMarcas']
    fecha = datetime.now()
    status = request.POST['txtStatus']
    # logo1 = request.POST['txtLogo1']
    logo1 = request.FILES['txtLogo1']
    

# ojo cambiar esto que es provisional
    request.session['empresa_id'] = 12
    empresa_id = request.session.get('empresa_id', None)
    if empresa_id is not None:
        empresa = Empresa.objects.get(id=empresa_id)
    else:
        return redirect('login')
    marca = Marca.objects.create(nombre=nombre, descripcion=descripcion, mostrarMarcas=mostrarMarcas, fecha=fecha, status=status, empresa_id=empresa, logo1=logo1)
    messages.success(request, '¡Marca guardada!')
    return redirect('/marca/')

def edicionMarca(request, id):
    marca = Marca.objects.get(id=id)
    return render(request, "edicionMarca.html", {"marca": marca})

def editarMarca(request):
    id= request.POST['txtId']
    nombre= request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    mostrarMarcas = request.POST['txtMostrarMarcas']
    fecha = datetime.now()
    status = request.POST['txtStatus']

    marca = Marca.objects.get(id=id)
    marca.nombre = nombre
    marca.descripcion = descripcion
    marca.mostrarMarcas = mostrarMarcas
    marca.fecha = fecha
    marca.status = status
    marca.save()
    messages.success(request, '¡Marca actualizada!')
    return redirect('/marca/')

def eliminacionMarca(request, id):
    marca = Marca.objects.get(id=id)
    marca.delete()
    messages.success(request, 'Marca eliminada!')
    return redirect('/marca/')