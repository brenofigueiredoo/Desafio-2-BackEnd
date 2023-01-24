from django.db import models
import uuid


class Transacoes_loja(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tipo = models.CharField(max_length=1)
    data = models.CharField(max_length=10)
    valor = models.FloatField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.CharField(max_length=8)
    dono_da_loja = models.CharField(max_length=15)
    nome_loja = models.CharField(max_length=19)
