from django.db import models

# Create your models here.
class Cadastro(models.Model):
    # Colunas no db:
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.nome}[{self.email}]'
    class Meta:
        # Nome Verboso do nosso Modelo:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        # Ordem decrescente:
        ordering = ['-data']


