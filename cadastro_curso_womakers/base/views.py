from django.shortcuts import render
# Importar Tabela http:
from django.http import HttpResponse

# Create your views here.
#Admin Padrão do Django
# http://127.0.0.1:8000/admin/login/?next=/admin/

#Tela 01 - Teste
# http://127.0.0.1:8000/inicio_teste
def inicio_teste(request):
    return HttpResponse('Olá mundo!')

#Tela 02 - Teste
# http://127.0.0.1:8000/inicioHtml
def inicioHtml(request):
    html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title> Cursos online </title>
        </head>
        <body>
            <h1> Olá Mundo! </h1>
        </body>
        </html
'''
    return HttpResponse(html)

#Tela 03 - Teste
# http://127.0.0.1:8000/inicioHtmlArq
def inicioHtmlArq(request):
    return render(request, 'inicioHtmlArq.html')

#Tela 04 - Valendo
# http://127.0.0.1:8000/
def inicio(request):
    return render(request, 'inicio.html')

#Tela 05 - Teste
# def cadastro(request):
    # pass

#Tela 06 - Valendo
# http://127.0.0.1:8000/cadastro
def cadastro(request):
    return render(request, 'cadastro.html')