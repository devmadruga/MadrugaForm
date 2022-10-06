from django.contrib import admin
from .models import Paciente
"""
Para registrar no admin a classe Paciente, precisei
1. criar o superusuário: python3 manage.py createsuperuser
2. Rodar: python manage.py makemigrations
4. Rodar: python manage.py migrate
"""

admin.site.register(Paciente)
