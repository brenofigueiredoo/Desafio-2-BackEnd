from rest_framework import serializers
from models import Transacoes_loja


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes_loja
        fields = "__all__"
        read_only_fields = ["id"]
