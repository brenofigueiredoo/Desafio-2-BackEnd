from rest_framework.views import Response, status, Request, APIView
from django.shortcuts import render
from django.http import HttpResponseRedirect
import ipdb

from .models import Transacoes_loja
from .serializer import LojaSerializer


def home(request: Request):
    return render(request, "home.html")


def cnab_tratada(request):
    with open("CNAB.txt", "wb") as file:
        for char in request.FILES["arquivoCnab"].chunks():
            file.write(char)

    data_transacoes = []

    with open("CNAB.txt", "r") as file:
        for char in file.read().split("\n"):

            valor_tratato = 0

            if len(char[9:19].split()) > 0:
                valor_tratato = int(char[9:19]) / 100

            data_transacoes.append(
                {
                    "tipo": char[0:1],
                    "data": f"{char[7:9]}/{char[5:7]}/{char[1:5]}",
                    "valor": valor_tratato,
                    "cpf": char[19:30],
                    "cartao": char[30:42],
                    "hora": f"{char[42:44]}:{char[44:46]}:{char[46:48]}",
                    "dono_da_loja": char[48:62].strip(),
                    "nome_loja": char[62:81],
                }
            )

        for char in data_transacoes:
            Transacoes_loja.objects.create(**char)

        return HttpResponseRedirect("/api/transacoes")


class TransacoesCnabView(APIView):
    def get(self, request: Request):
        queryset = Transacoes_loja.objects.all()
        serializer = LojaSerializer(queryset, many=True)

        valor_saida = 0
        valor_entrada = 0
        for char in queryset:
            if char.tipo in "239":
                valor_saida += char.valor
            else:
                valor_entrada += char.valor

        valor_total = valor_entrada - valor_saida

        return Response({"valor_total": valor_total, "data": serializer.data})
