from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Funcionario

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"

class FuncionarioDetailView(DetailView): 
    model = Funcionario 
    template_name = "lista_funcionario.html" 
    context_object_name = "fun"    

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ("nome", "cpf", "email", "remuneracao")
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")