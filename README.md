EcommercePython

# Crud completo con Django, SQLite3 ORM, Bootstrap y Javascript

## Creamos un projecto

c:\djangoproject> django-admin startproject shoppingcart
cd shoppingcart

## Creamos una app categories

python manage.py startapp categories

## Settings.py

### Agregamos la app categories

40 'categories'

### Agregamos la bd

80 'name': 'ecommerce.db'

### Agregamos el time_zone

107 TIME_ZONE: 'America/Argentina/Buenos_Aires'

## Models.py

Lo generamos desde nuestra base de datos en mysql con la ayuda de chatgpt.

### Creamos la clase Categorias

```
class Categorias(models.Model):
nombre = models.CharField(max_length=100)
descripcion = models.TextField()
imagen = models.CharField(max_length=50, default='sinimagen.png')
promocion = models.IntegerField(choices=((0, 'Normal'), (1, 'Promoción (categoria del mes)')), default=1)
fecha = models.DateTimeField()
status = models.IntegerField(choices=((0, 'Inactivo'), (1, 'Activo'), (2, 'Eliminado')), default=0)
idEmpresa = models.CharField(max_length=100)
```

    def __str__(self):
        texto = "{0} - {1} - ({2})"
        return texto.format(self.nombre, self.descripcion, self.idEmpresa)

## Admin.py

Registramos el modelo para verlo en el panel de administración

```
from django.contrib import admin

from .models import Categorias

admin.site.register(Categorias)
```

## Realizamos la migración

### Desde la consola

c:\djangoproject>
python manage.py migrate

python manage.py makemigrations

## Creamos un superusuario

python manage.py createsuperuser

```
user: gustabin
email: tabindev@gamil.com
pass: 1234567890
```

**Realizamos la migración nuevamente**

python manage.py migrate

## Arrancamos el servidor

python manage.py runserver

Desde 127.0.0.1:8000 o localhost:8000 podemos acceder a nuestra App

si le agregamos /admin entonces podemos ingresar al panel de administración
127.0.0.1:8000/admin

Colocamos las credenciales y podemos ver nuestra tabla categoriass

## Crear template dentro de categories

Creamos el directorio **templates**

## Crear gestionCategorias.html dentro de templates

Creamos el archivo **gestionCategorias.html**
con la tecla ! conseguimos la estructura html5 y le agregamos en el body un h1 **Página de gestionCategorias**

## Crear urls.py dentro de categories

Creamos el archivo **urls.py**

```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

## Desde views.py

Creamos el método home

```
from django.shortcuts import render

def home(request):
    return render(request, "gestionCategorias.html")
```

## Desde urls.py **"del proyecto"**

Agregamos la ruta de **categories**

```
from django.urls import path, include

urlpatterns = [
    path('', include('categories.urls'))
]
```

## Mostramos el listado de las categorias

Desde **views.py** importamos el modelo _categorias_

```
from .models import Categorias
```

En la variable **categoriaListado** vamos a almacenar una lista con todas las categorias

```
 categoriasListado = Categorias.objects.all()
```

Le enviamos esta lista al template asi:

```
  return render(request, "gestionCategorias.html", {"categorias": categoriasListado})
```

## Mostramos la lista en el template

En **gestionCategorias.html**

```
<ul>
    {% for c in categorias %}
        <li>{{ c.nombre }}</li>
        <li>{{ c.descripcion }}</li>
        <li>{{ c.idEmpresa }}</li>
    {% endfor %}
</ul>
```

## Le damos estilo con bootstrap

Desde **getbootstrap.com** en getting start copiamos el css y lo pegamos en gestionCategorias.html despues del < title >

```
    <link
      rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous"
    />
```

Y copiamos los js y los pegamos antes del < /body>

```
<script
      src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js"
      integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
      integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js"
      integrity="sha384-+sLIOodYLS7CIrQpBjl+C7nPvqq+FbNUBDunl/OZv93DB7Ln/533i8e/mZXLi/P+"
      crossorigin="anonymous"
    ></script>
```

## Creamos un template base

Dentro de **templates** creamos base.html
Cortamos todo el contenido de gestionCategorias.html y lo pegamos en base.html

Reemplazamos el contenido del body con:

```
{% block body %}

{% endblock %}
```

Desde **getbootstrap.com** buscamos un ejemplo del componente navbar, lo copiamos y lo pegamos antes de {% block body %} en base.html

## Importamos el template base.html en gestionCategorias.html

Desde gestionCategorias.html

```
{% extends "./base.html"%}
```

Creamos un formulario dentro del block

```
{% block body%}

{% endblock %}
```

Quedaría asi:

```
{% block body%}
    <form action="/registrarCategoria/" method="POST">
          {% csrf_token %}
          <div class="form-group">
            <input
              type="text"
              id="txtNombre"
              name="txtNombre"
              class="form-control"
              placeholder="Nombre"
              minlength="3"
              maxlength="100"
              required
            />
          </div>
          <div class="form-group">
            <input
              type="text"
              id="txtDescripcion"
              name="txtDescripcion"
              class="form-control"
              placeholder="Descripción"
              minlength="3"
              required
            />
          </div>
          <div class="form-group">
            <input
              type="text"
              id="txtIdEmpresa"
              name="txtIdEmpresa"
              class="form-control"
              minlength="3"
              maxlength="100"
              required
            />
          </div>
          <div class="form-group">
            <button type="submit"
            class="btn btn-success
            btn-block text-white">
              Guardar
            </button>
          </div>
    </form>
{% endblock %}
```

_Debemos hacer nuevamente el listado de las categorias pero esta vez usaremos una tabla y crearemos dos columnas una para el formulario y otra para el listado._

## Crearemos la ruta registrarCategoria _(la necesita el formulario en el action)_

Desde urls.py agregamos

```
  path('registrarCategoria/', views.registrarCategoria),
```

## Creamos registrarCategoria dentro de views.py

Necesitamos importar redirect y datetime

```
from django.shortcuts import render, redirect
from datetime import datetime

def registrarCategoria(request):
    nombre= request.POST['txtNombre']
    descripcion = request.POST['txtDescripcion']
    idEmpresa = request.POST['txtIdEmpresa']
    fecha = datetime.now()

    categoria = Categorias.objects.create(nombre=nombre, descripcion=descripcion, idEmpresa=idEmpresa, fecha=fecha)

    return redirect('/')
```

## Agregamos los botones de Editar y Eliminar en gestionCategorias.html

En gestionCategorias.html agregamos al <thead> un <th>

```
 <th colspan="2">Opciones</th>
```

y al <tbody> le agregamos dos <td>

```
<td>
   <a href="edicionCategoria/{{c.id}}" class="btn btn-info">
       Editar
   </a>
</td>
<td>
   <a href="eliminacionCategoria/{{c.id}}" class="btn btn-danger">
       Eliminar
   </a>
</td>
```

## Creamos la ruta para eliminacionCategoria en urls.py

```
path('eliminacionCategoria/<id>', views.eliminacionCategoria),
```

## Creamos la vista eliminacionCategoria en views.py

```
def eliminacionCategoria(request, id):
    categoria = Categorias.objects.get(id=id)
    categoria.delete()
    return redirect('/')
```

## Creamos la ruta para edicionCategoria en urls.py

```
 path('edicionCategoria/<id>', views.edicionCategoria),
```

## Creamos la vista edicionCategoria en views.py

```
def edicionCategoria(request, id):
    categoria = Categorias.objects.get(id=id)
    return render(request, "edicionCategoria.html", {"categoria": categoria})
```

## Creamos la vista edicionCategorias.html dentro de templates

Le agregamos al principio

```
{% extends "./base.html" %}
<!-- {% block title %}
Gestión de categorias
{% endblock%}  -->
{% block body %}

 <!-- Aqui va el código -->

{% endblock%}
```

Vamos a incorporar el componente card de bootstrap y a centrar el contenido con offset-md-4 asi:

```
<div class="row">
  <div class="col-md-4 offset-md-4">
    <h2>Edición de categorias</h2>
    <div class="card">
      <div class="card-body">

        <!-- Aqui va el formulario -->

      </div>
    </div>
  </div>
</div>
```

Luego copiamos el formulario de gsitionCategorias.html y lo pegamos en el card-body.

```
<form action="/editarCategoria/" method="POST">
          {% csrf_token %}
          <div class="form-group">
            <input
              type="text"
              id="txtId"
              name="txtId"
              class="form-control"
              placeholder="Id"
              minlength="3"
              maxlength="100"
              required
              value="{{categoria.id}}"
              readonly
            />
          </div>
          <div class="form-group">
            <input
              type="text"
              id="txtNombre"
              name="txtNombre"
              class="form-control"
              placeholder="Nombre"
              minlength="3"
              maxlength="100"
              required
              value="{{categoria.nombre}}"
            />
          </div>
          <div class="form-group">
            <input
              type="text"
              id="txtDescripcion"
              name="txtDescripcion"
              class="form-control"
              placeholder="Descripción"
              minlength="3"
              required
              value="{{categoria.descripcion}}"
            />
          </div>
          <div class="form-group">
            <input
              type="text"
              id="txtIdEmpresa"
              name="txtIdEmpresa"
              class="form-control"
              minlength="3"
              maxlength="100"
              required
              value="{{categoria.idEmpresa}}"
            />
          </div>
          <div class="form-group">
            <button type="submit" class="btn btn-success btn-block text-white">
              Guardar
            </button>
          </div>
</form>
```

Se agrego una ruta al action y un value a c/u de los campos

value="{{categoria.id}}"

value="{{categoria.nombre}}"

value="{{categoria.descripcion}}"

value="{{categoria.idEmpresa}}"

El campo id debe ser de solo lectura por eso se coloco el atributo readonly.

Como usamos esta ruta /editarCategoria/ en el form debemos crearla.

```
<form action="/editarCategoria/" method="POST">
```

## Creamos la ruta para editarCategoria en urls.py

```
 path('editarCategoria/', views.editarCategoria)
```

## Creamos la vista editarCategorias en views.py

```
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
    return redirect('/')
```

Estamos recibiendo el id y lo usamos para buscarlo en id=id

## Le ponemos # al < thead > en gestionCategorias.html

Antes de

```
<th>Nombre</th>
```

colocamos

```
<th>#</th>
```

Y en el < tbody > antes de

```
<td>{{c.nombre}}</td>
```

colocamos

```
<td>{{forloop.counter}}</td>
```

## Vamos a centrar los elementos de la tabla

Dentro de la carpeta categories creamos la carpeta static y dento de ella las carpetas js, css y img.

En la carpeta css creamos el archivo **gestionCategorias.css**

```
th,
td {
  text-align: center;
  vertical-align: middle;
}
```

# Importamos el css en el template base.html

Luego del < head > colocamos

```
{% load static %}
```

antes del </ head > colocamos

```
<link rel="stylesheet" href="{% static 'css/gestionCategorias.css' %}" />
```

## Crear una ventana de confirmación antes de borrar

En gestionCategorias.html le agregamos la clase **btnEliminacion** al botón eliminar.

```
<a href="eliminacionCategoria/{{c.id}}" class="btn btn-danger btnEliminacion" >Eliminar</a>
```

Esta clase servirá como selector.

En el directorio js crearemos el archivo gestionarCategorias.js

```
(function () {
  const btnEliminacion = document.querySelectorAll('.btnEliminacion');
  btnEliminacion.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const confirmacion = confirm('Seguro de eliminar el registro?');
      if (!confirmacion) {
        e.preventDefault();
      }
    });
  });

  $(document).ready(function () {
    // Oculta la alerta después de 3 segundos
    setTimeout(function () {
      $('.alert').alert('close');
    }, 3000);
  });
})();
```

# Importamos el js en el template base.html

Antes del < /body > colocamos

```
<script src="{% static 'js/gestionCategorias.js' %}"></script>
```

## Mostrar mensajes emergentes que indiquen las acciones que se están realizando

En gestionCategorias.html antes del

```
<h2>Gestión de categorias</h2>
```

colocamos

```
{% if messages %}
    {% for message in messages %}
        <div class="alert alert-dismissible alert-success">
        <button type="button" class="close" data-dismiss="alert">&times;</button>
        <strong class="text-dark">{{ message }}</strong>
        </div>
    {% endfor %}
{% endif %}
```

Para poder enviar los mensajes debemos importarlos en _views.py_

```
from django.contrib import messages
```

En c/u de las vistas debemos invocarlos antes del return

```
10 messages.success(request, '¡Categorias listadas!')
20 messages.success(request, '¡Categoria guardada!')
38 messages.success(request, '¡Categoria actualizada!')
44 messages.success(request, '¡Categoria eliminada!')
```

Realizado por Gustavo Arias gustavoarias@outlook.com Sigueme en youtube @guskit
