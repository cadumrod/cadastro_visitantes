from django.forms import ModelForm
from .models import Visitante

class VisitanteForm(ModelForm):
    class Meta:
        model = Visitante
        fields = '__all__'