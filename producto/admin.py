from django.contrib import admin
from .models import Producto
from .models import Color
from .models import Talla

# Register your models here.
admin.site.register(Producto)
admin.site.register(Color)
admin.site.register(Talla)