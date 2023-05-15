from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarProducto/', views.registrarProducto),
    path('eliminacionProducto/<id>', views.eliminacionProducto),
    path('edicionProducto/<id>', views.edicionProducto),
    path('editarProducto/', views.editarProducto), 
]

