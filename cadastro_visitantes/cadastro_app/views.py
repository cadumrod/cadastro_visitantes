from django.shortcuts import render, redirect, HttpResponse
from .models import Visitante
from .forms import VisitanteForm
import re
from django.contrib.auth.decorators import login_required


def visitantes(request):
    dados = {
        'dados': Visitante.objects.all()
    }
    return render(request, 'cadastro_visitante/visitantes.html', context= dados)

@login_required
def detalhe(request, id_visitante):
    dados = {
        'dados': Visitante.objects.get(pk=id_visitante)
        }
    return render(request, 'cadastro_visitante/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        visitante_form = VisitanteForm(request.POST)
        if visitante_form.is_valid():
            visitante_form.save()
        return redirect('visitantes')
    
    else:
        visitante_form = VisitanteForm()
        formulario = {
            'formulario': visitante_form
        }
        return render(request, 'cadastro_visitante/cadastro.html', context=formulario)
    
@login_required
def editar(request, id_visitante):
    visitante = Visitante.objects.get(pk=id_visitante)
    if request.method == 'GET':
       formulario = VisitanteForm(instance=visitante)
       return render (request, 'cadastro_visitante/cadastro.html', {'formulario':formulario})
    else:
        formulario = VisitanteForm(request.POST, instance=visitante)
        if formulario.is_valid():
            formulario.save()
            return redirect('visitantes')
        

def excluir(request, id_visitante):
    visitante = Visitante.objects.get(pk=id_visitante)
    if request.method == 'POST':
        visitante.delete()
        return redirect('visitantes')
    return render(request,'cadastro_visitante/confirmar_exclusao.html',{'item': visitante})