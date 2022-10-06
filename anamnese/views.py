from django.shortcuts import render
from django.http import HttpResponse
from .models import Paciente
from django.views.generic import CreateView


class PacienteCreate(CreateView):
    """
    As CreatView esperam encontrar um template com nome 'model_form.html'.
    Como o nome do model é Paciente, ela espera 'paciente_form.html'.
    """
    model = Paciente
    fields = '__all__'
