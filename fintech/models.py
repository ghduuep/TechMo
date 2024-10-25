from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.TextField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    TIPOS = (
        ('E', 'ENTRADA'),
        ('S', 'SAIDA'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    tipo = models.CharField(max_length=1, choices=TIPOS, default='S')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    data_transacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transacao de R${self.valor} feita por {self.usuario}'

