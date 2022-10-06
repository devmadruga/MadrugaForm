from django.db import models
from django.urls import reverse

class Paciente(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("paciente_detail", kwargs={"pk": self.pk})