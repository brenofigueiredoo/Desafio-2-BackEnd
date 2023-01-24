from rest_framework.views import Response, status, Request, APIView
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponseRedirect
import ipdb
from .models import Transacoes_loja
from datetime import datetime, timedelta, date


def home(request: Request):
    return render(request, "home.html")


def transacoes(request: Request):
    return render(request, "transacoes.html")


def cnab_tratada(request):
    # with open("CNAB.txt", "w") as file:

    #     for char in request.FILES["arquivoCnab"].chunks():
    #         ipdb.set_trace()
    #         file.write(char)

    data_transacoes = []

    with open("CNAB.txt", "r") as file:
        for char in file.read().split("\n"):

            valor_tratato = []

            if type(char[9:19]) == str:
                valor_tratato.append(int(char[9:19]) / 100)

            data_transacoes.append(
                {
                    "tipo": char[0:1],
                    "data": f"{char[7:9]}/{char[5:7]}/{char[1:5]}",
                    "valor": valor_tratato[0],
                    "cpf": char[19:30],
                    "cartao": char[30:42],
                    "hora": f"{char[42:44]}:{char[44:46]}:{char[46:48]}",
                    "dono_da_loja": char[48:62].strip(),
                    "nome_loja": char[62:81],
                }
            )

            print(data_transacoes)
        # for char in data_transacoes:
        #     Transacoes_loja.objects.create(**char)

        return HttpResponseRedirect("/transacoes/")


class TransacoesCnabView(viewsets.ModelViewSet):
    ...
