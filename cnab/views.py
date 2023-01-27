from rest_framework.views import Response, Request, APIView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Transacoes_loja
from .serializer import LojaSerializer
import ipdb


def home(request: Request):
    return render(request, "home.html")


def cnab_tratada(request):
    with open("CNAB.txt", "wb") as file:
        for char in request.FILES["arquivoCnab"].chunks():
            file.write(char)

    data_transacoes = []

    with open("CNAB.txt", "r") as file:
        for loja in file.read().split("\n"):

            # ipdb.set_trace()
            valor_tratato = 0

            if len(loja[9:19].split()) > 0:
                valor_tratato = int(loja[9:19]) / 100

            data_transacoes.append(
                {
                    "tipo": loja[0:1],
                    "data": f"{loja[7:9]}/{loja[5:7]}/{loja[1:5]}",
                    "valor": valor_tratato,
                    "cpf": loja[19:30],
                    "cartao": loja[30:42],
                    "hora": f"{loja[42:44]}:{loja[44:46]}:{loja[46:48]}",
                    "dono_da_loja": loja[48:62].strip(),
                    "nome_loja": loja[62:81],
                    "nome_loja": " ".join(loja[62:81].split()),
                }
            )

        for char in data_transacoes:
            Transacoes_loja.objects.create(**char)

        return HttpResponseRedirect("/api/transacoes")


class TransacoesCnabView(APIView):
    def get(self, request: Request):
        queryset = Transacoes_loja.objects.all()
        serializer = LojaSerializer(queryset, many=True)

        data = {}

        valor_saida = 0
        valor_entrada = 0
        for char in queryset:
            data[char.nome_loja] = 0

        for char in queryset:
            if char.tipo in "239":
                data[char.nome_loja] -= char.valor
                valor_saida += char.valor
            else:
                data[char.nome_loja] += char.valor
                valor_entrada += char.valor

        for char in queryset:
            data[char.nome_loja] = round(data[char.nome_loja], 2)

        valor_total = valor_entrada - valor_saida

        return Response(
            {
                "valor_total": valor_total,
                "valor_total_loja": data,
                "data": serializer.data,
            }
        )
