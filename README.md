# Projeto Django - Atividade Final de Desenvolvimento de Aplicações

Este repositório contém o código de um projeto desenvolvido em Python, utilizando o framework Django e um banco de dados MySQL. O objetivo do projeto é implementar um CRUD básico para atender aos requisitos da atividade final da disciplina de Desenvolvimento de Aplicações.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do backend.
- **Django**: Framework web utilizado para a construção da aplicação, proporcionando uma estrutura robusta e eficiente.
- **MySQL**: Sistema de gerenciamento de banco de dados relacional utilizado para armazenar as informações da aplicação.

## Funcionalidades

Este projeto implementa um CRUD (Criar, Ler, Atualizar, Deletar) básico, permitindo a manipulação de registros em um banco de dados MySQL. As funcionalidades incluem:

1. **Cadastro de novos registros**.
2. **Exibição de registros existentes**.
3. **Edição de registros já cadastrados**.
4. **Exclusão de registros**.

Essas operações são acessadas via interface web, desenvolvida com as ferramentas e estruturas do Django.

## Estrutura do Projeto

O projeto segue a estrutura padrão do Django, com os seguintes diretórios principais:

- `app/`: Contém a lógica da aplicação, como modelos, visões e templates.
- `funcionarios/`: Contém configurações principais do Django, como o arquivo `settings.py`, onde as configurações do banco de dados e outras opções importantes estão definidas.
- `manage.py`: Script para executar o servidor e outros comandos do Django.

## Como Executar o Projeto

1. Clone este repositório em sua máquina local:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use venv\Scripts\activate
   ```

4. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure o banco de dados no arquivo `settings.py`. No Django, a configuração do MySQL pode ser feita da seguinte forma:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nome_do_banco',
           'USER': 'usuario',
           'PASSWORD': 'senha',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. Aplique as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento do Django:
   ```bash
   python manage.py runserver
   ```

8. Abra o navegador e acesse:
   ```
   http://127.0.0.1:8000/app/lista_funcionarios
   ```
