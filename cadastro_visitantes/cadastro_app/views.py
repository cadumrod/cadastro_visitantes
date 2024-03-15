from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Visitante
from .forms import VisitanteForm
from django.contrib.auth.decorators import login_required

@login_required
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
        
#@login_required
#def excluir(request, id_visitante):
#    visitante = Visitante.objects.get(pk=id_visitante)
#    if request.method == 'POST':
#        visitante.delete()
#        return redirect('visitantes')
#    return render(request,'cadastro_visitante/confirmar_exclusao.html',{'item': visitante})


@login_required
def excluir(request, id_visitante):
    # Identifique o usuário específico
    admin = 'admin'  # Substitua pelo nome de usuário ou ID do usuário específico
    
    # Verifique se o usuário atual é o usuário específico
    if request.user.username != admin:
        return redirect('permissao_negada')  # Redirecione para uma página de permissão negada
    
    visitante = get_object_or_404(Visitante, pk=id_visitante)
    if request.method == 'POST':
        visitante.delete()
        return redirect('visitantes')
    return render(request, 'cadastro_visitante/confirmar_exclusao.html', {'item': visitante})


def permissao_negada(request):
    return render(request, 'cadastro_visitante/permissao_negada.html')
