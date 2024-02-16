from django import forms
from base.models import Cadastro

class CadastroForm(forms.ModelForm):
    # A Classe Meta existe para eivitar repetição de código
    class Meta:
        #Models=Tabelas
        model = Cadastro
        #Fields=Campos
        fields = ['nome', 'email', 'senha']
        # Para resolver o disfarce da senha que tinha sumido!!
        widgets = {'senha': forms.PasswordInput}

#Este é o padrão que evita repetição de código conforme ocorre no arquivo: forms_duplicando.py

    # De preferência o HTML só deve renderizar a aparencia, evitar que tenham informações.
    # Verificar a documentação Django Forms para ver a lista de tipos de (email, senha...)
    # Pesquisar depois modos de segurança para forms