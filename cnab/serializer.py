from rest_framework import serializers
from .models import Transacoes_loja


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes_loja
        fields = (
            "id",
            "tipo",
            "data",
            "valor",
            "cpf",
            "cartao",
            "hora",
            "dono_da_loja",
            "nome_loja",
        )
