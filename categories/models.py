from django.db import models

from empresa.models import Empresa

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="categoria", null=True, blank=True, default='sinimagen.png')
    promocion = models.IntegerField(choices=((0, 'Normal'), (1, 'Promoción (categoria del mes)')), default=1)
    fecha = models.DateTimeField()
    status = models.IntegerField(choices=((0, 'Inactivo'), (1, 'Activo'), (2, 'Eliminado')), default=0)
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} - {1} - ({2})"
        return texto.format(self.nombre, self.descripcion, self.idEmpresa)
