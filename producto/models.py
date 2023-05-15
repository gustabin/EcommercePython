from django.db import models
from categories.models import Categorias
from empresa.models import Empresa
from marca.models import Marca

class Color(models.Model):
    nombre = models.CharField(max_length=50)
    # otros campos que puedan tener los colores
    
    def __str__(self):
        return self.nombre

class Talla(models.Model):
    nombre = models.CharField(max_length=50)
    # otros campos que puedan tener las tallas
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.TextField()
    especificacion = models.CharField(max_length=3000)
    marca_id = models.ForeignKey(Marca, on_delete=models.CASCADE)
    color_id = models.ForeignKey(Color, on_delete=models.CASCADE)
    talla_id = models.ForeignKey(Talla, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="producto", null=True, blank=True, default='sinimagen.png')
    categoria_id = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=30)
    promocion = models.BooleanField(default=True)
    stock = models.IntegerField()
    orden = models.IntegerField(default=99)
    fecha = models.DateTimeField()
    status = models.IntegerField(default=0) # 0= Inactivo, 1=Activo, 2=Eliminado
    calificacion = models.IntegerField(default=0)
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} - {1} - ({2})"
        return texto.format(self.nombre, self.empresa_id, self.precio)
