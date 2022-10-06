from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('cadastrar_paciente/', views.PacienteCreate.as_view(), name='cadastrar_paciente')          
]
