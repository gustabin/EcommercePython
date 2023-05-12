from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarEmpresa/', views.registrarEmpresa),
    path('eliminacionEmpresa/<id>', views.eliminacionEmpresa),
    path('edicionEmpresa/<id>', views.edicionEmpresa),
    path('editarEmpresa/', views.editarEmpresa), 
]
