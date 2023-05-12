from django.db import models

from empresa.models import Empresa

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    logo1 = models.CharField(max_length=50, null=True, blank=True)
    logo2 = models.CharField(max_length=50, null=True, blank=True)
    logo3 = models.CharField(max_length=50, null=True, blank=True)
    logo4 = models.CharField(max_length=50, null=True, blank=True)
    logo5 = models.CharField(max_length=50, null=True, blank=True)
    logo6 = models.CharField(max_length=50, null=True, blank=True)
    logo7 = models.CharField(max_length=50, null=True, blank=True)
    logo8 = models.CharField(max_length=50, null=True, blank=True)
    logo9 = models.CharField(max_length=50, null=True, blank=True)
    logo10 = models.CharField(max_length=50, null=True, blank=True)
    logo11 = models.CharField(max_length=50, null=True, blank=True)
    logo12 = models.CharField(max_length=50, null=True, blank=True)
    mostrarMarcas = models.IntegerField(default=1, null=True, blank=True, verbose_name="Mostrar")
    fecha = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(default=0, choices=((0, 'Inactivo'), (1, 'Activo'), (2, 'Eliminado')))
    empresa_id = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    def __str__(self):
        texto = "{0} - {1} - ({2})"
        return texto.format(self.titulo, self.empresa, self.mostrarMarcas)

