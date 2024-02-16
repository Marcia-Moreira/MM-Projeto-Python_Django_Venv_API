# VIA MAIS ESCRITA COM TRECHOS DESNECESSÁRIOS:
from django import forms

class CadastroForm(forms.Form):

    nome = forms.CharField()
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
    
    #Este é o padrão que REPETE código conforme NÃO acontece arquivo: forms.py

    # De preferência o HTML só deve renderizar a aparencia, evitar que tenham informações.
    # Verificar a documentação Django Forms para ver a lista de tipos de (email, senha...)
    # Pesquisar depois modos de segurança para forms