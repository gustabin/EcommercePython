from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarMarca/', views.registrarMarca),
    path('eliminacionMarca/<id>', views.eliminacionMarca),
    path('edicionMarca/<id>', views.edicionMarca),
    path('editarMarca/', views.editarMarca), 
    path('upload/', views.upload, name='upload'),
]
