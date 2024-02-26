from django.db import models
from datetime import datetime

"""
Data
Tipo
Nome
Rg
Motivo
"""





class Visitante(models.Model):
    tipo_visitante = [
        ('civil', 'Civil'),
        ('militar', 'Militar')
    ]
    tipo = models.CharField(max_length=10, choices=tipo_visitante)
    nome = models.TextField(max_length=255)
    rg = models.IntegerField()
    motivo = models.TextField(max_length=255)
    data = models.DateField(default=datetime.now)
