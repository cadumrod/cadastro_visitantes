from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse('Página de teste')

def pagina_contato(request):
    return HttpResponse('Entre em contato com o Setor de T.I')

def pagina_de_cadastro(request):
    return render(request, 'cadastro_visitante/visitantes.html')