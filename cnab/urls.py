from django.urls import path
from . import views

urlpatterns = [
    path("api/transacoes/", views.TransacoesCnabView.as_view({"get": "list"})),
    path("", views.home, name="home"),
    path("cnab_tratada/", views.cnab_tratada, name="cnab_tratada"),
    path("transacoes/", views.transacoes, name="transacoes"),
]
