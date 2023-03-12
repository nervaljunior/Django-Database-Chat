
from django.db import models

class Carros(models.Model):
    modelo = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    ano = models.IntegerField()