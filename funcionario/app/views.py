from django.shortcuts import render

from django.views.generic import CreateView, ListView
from .models import Funcionario

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"
