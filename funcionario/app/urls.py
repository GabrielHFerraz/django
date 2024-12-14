from django.urls import path, include
from .views import FuncionarioCreateView, FuncionarioListView

urlpatterns = [
    path("form_funcionario", FuncionarioCreateView.as_view()),
    path('lista_funcionarios', FuncionarioListView.as_view(), name = "lista_funcionarios"),
]