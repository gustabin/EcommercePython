from django.shortcuts import render, redirect
from .models import Producto
from empresa.models import Empresa
from datetime import datetime
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore
from django.core.files.storage import FileSystemStorage
from .models import Color
from .models import Talla
from .models import Categorias
from .models import Marca


def home(request):
    productoListado = Producto.objects.all()
    categoria = Categorias.objects.all()
    colores = Color.objects.all()
    tallas = Talla.objects.all()
    marcas = Marca.objects.all()
    messages.success(request, 'Productos listados!')
    return render(request, "gestionProducto.html", {"productos": productoListado, "categorias": categoria, "colores": colores, "tallas": tallas, "marcas": marcas})

def registrarProducto(request):
    nombre= request.POST['txtNombre']
    precio = request.POST['txtPrecio']
    precio_decimal = float(precio.replace(',', '.'))
    descripcion = request.POST['txtDescripcion']
    especificacion = request.POST['txtEspecificacion']
    marca_id = request.POST['txtMarca_id']
    color_id = request.POST['txtColor_id']
    color = Color.objects.get(id=color_id)
    talla_id = request.POST['txtTalla_id']
    talla = Talla.objects.get(id=talla_id)
    categoria_id = request.POST['txtCategoria_id']
    categoria = Categorias.objects.get(id=categoria_id)
    codigo = request.POST['txtCodigo']
    promocion = request.POST['txtPromocion']
    stock = request.POST['txtStock']
    orden = request.POST['txtOrden']
    fecha = datetime.now()
    status = request.POST['txtStatus']
    calificacion = request.POST['txtCalificacion']
    imagen = request.FILES.get('txtImagen', 'marcas/sinimagen.png')  

# ojo cambiar esto que es provisional
    request.session['empresa_id'] = 26
    empresa_id = request.session.get('empresa_id', None)
    if empresa_id is not None:
        empresa = Producto.objects.get(id=empresa_id)
    else:
        return redirect('login')
    producto = Producto.objects.create(nombre=nombre, precio=precio_decimal, descripcion=descripcion, especificacion=especificacion, 
                                       marca_id=marca_id, color_id=color, talla_id=talla, categoria=categoria,
                                       codigo=codigo, promocion=promocion, stock=stock, orden=orden, fecha=fecha, 
                                       status=status, calificacion=calificacion, empresa_id=empresa, imagen=imagen)
    messages.success(request, '¡producto guardado!')
    return redirect('/producto/')

def edicionProducto(request, id):
    producto = Producto.objects.get(id=id)
    colores = Color.objects.all()
    tallas = Talla.objects.all()
    categoria = Categorias.objects.all()
    marcas = Marca.objects.all()
    
    return render(request, 'edicionProducto.html', {'producto': producto, 'colores': colores, 
                                                    'tallas': tallas, 'categorias': categoria, 'marcas': marcas})

def editarProducto(request):
    id= request.POST['txtId']
    nombre= request.POST['txtNombre']
    precio = request.POST['txtPrecio']
    precio_decimal = float(precio.replace(',', '.'))
    descripcion = request.POST['txtDescripcion']
    especificacion = request.POST['txtEspecificacion']
    marca_id = request.POST['txtMarca_id']
    color_id = request.POST['txtColor_id']
    color = Color.objects.get(id=color_id)
    talla_id = request.POST['txtTalla_id']
    talla = Talla.objects.get(id=talla_id)
    categoria_id = request.POST['txtCategoria_id']
    categoria = Categorias.objects.get(id=categoria_id)
    codigo = request.POST['txtCodigo']
    promocion = request.POST['txtPromocion']
    stock = request.POST['txtStock']
    orden = request.POST['txtOrden']
    fecha = datetime.now()
    status = request.POST['txtStatus']
    calificacion = request.POST['txtCalificacion']
    # empresa_id = request.POST['txtEmpresa_id'] 
    
    producto = Producto.objects.get(id=id)
    producto.nombre = nombre
    producto.precio = precio_decimal
    producto.descripcion = descripcion
    producto.especificacion = especificacion
    # producto.marca_id = marca_id
    producto.color_id = color
    producto.talla_id = talla
    producto.categoria_id = categoria
    producto.codigo = codigo
    producto.promocion = promocion
    producto.stock = stock
    producto.orden = orden
    producto.fecha = fecha
    producto.status = status
    producto.calificacion = calificacion
    # producto.empresa_id = empresa_id

    if 'txtImagen' in request.FILES:
        imagen = request.FILES['txtImagen']
        producto.imagen = imagen   
    producto.save()
    messages.success(request, '¡Producto actualizado!')
    return redirect('/producto/')

def eliminacionProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, 'Producto eliminado!')
    return redirect('/producto/')