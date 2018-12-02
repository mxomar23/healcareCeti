from django.urls import path
from .views import *
from django.contrib.auth.views import auth_login

app_name = 'pacientes'
urlpatterns = [
    path('', index, name='paciente-index'),
    path('lista', PacienteListView.as_view(), name='paciente-lista'),
    path('perfil/<int:pk>/', PacienteDetailView.as_view(), name='paciente-perfil'),
    path('agregar/<int:pk>/', agregar_paciente, name='paciente-agregar'),
    path('buscar', buscar_paciente, name='paciente-buscar'),
]
