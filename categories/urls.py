from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCategoria/', views.registrarCategoria),
    path('eliminacionCategoria/<id>', views.eliminacionCategoria),
    path('edicionCategoria/<id>', views.edicionCategoria),
    path('editarCategoria/', views.editarCategoria)
]
