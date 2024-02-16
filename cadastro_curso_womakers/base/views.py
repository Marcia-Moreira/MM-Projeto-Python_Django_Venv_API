# VIA MAIS LIMPA:
from django.shortcuts import render
# Importar Tabela http:
from django.http import HttpResponse
from base.forms_duplicando import CadastroForm
#Importar a nova models/tabela:
from base.models import Cadastro

# Create your views here.

#Tela 01 - Início
# http://127.0.0.1:8000/
def inicio(request):
    return render(request, 'inicio.html')

#Tela 02 - Cadastro Usuário
# http://127.0.0.1:8000/cadastro
def cadastro(request):
    sucesso = False
    # form = CadastroForm(request.POST or None)
    form = CadastroForm(request.POST)
    if form.is_valid():
        sucesso = True
        form.save()
        # Não funciona. coloquei essa linha mas não funciona
        return render (request, 'inicio.html')  # Redirecionar para a página de início após o sucesso do cadastro
    else:
        form = CadastroForm()
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    # Renderizar a página 'cadastro.html' com o contexto
    return render(request, 'cadastro.html', contexto)