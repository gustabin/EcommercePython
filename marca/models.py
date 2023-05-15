from django.db import models

from empresa.models import Empresa

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="marcas", null=True, blank=True)
    mostrarMarcas = models.IntegerField(default=1, null=True, blank=True, verbose_name="Mostrar")
    fecha = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0, choices=((0, 'Inactivo'), (1, 'Activo'), (2, 'Eliminado')))
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} - {1} - ({2})"
        return texto.format(self.nombre, self.empresa_id, self.mostrarMarcas)

