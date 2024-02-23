from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Página de teste')

def pagina_contato(request):
    return HttpResponse('Entre em contato com o Setor de T.I')

def consulta_visitantes(request):
    visitantes = {
        'tipo_cadastro': request.POST.get('Tipocadastro'),
        'nome_cadastro': request.POST.get('Nomecadastro'),
        'rg_cadastro': request.POST.get('Rgcadastro'),
        'motivo_cadastro': request.POST.get('Motivocadastro')
    }
    return render(request, 'cadastro_visitante/consulta_visitantes.html', visitantes)


def cadastrar_visitante(request):
    return render(request, 'cadastro_visitante/cadastro.html')