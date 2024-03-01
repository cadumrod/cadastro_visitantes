from django.forms import ModelForm
from .models import Visitante
from django import forms

class VisitanteForm(ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'