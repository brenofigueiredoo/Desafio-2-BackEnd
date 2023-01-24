
# Sobre o projeto

Nesse projeto foi desenvolvido uma interface web que aceita upload do arquivo CNAB, com os dados das movimentações financeiras de várias lojas. A aplicação faz a tratativa dos dados e armazena-os em um banco de dados relacional e exibe essas informaçes em tela.

# Funcionalidades



# Tecnologias utilizadas

- Python 3.11.1
- Django RestFramework
- SQLite

# Passos de instalação

    1- Clone o repositório para a sua máquina
    2- Crie um ambiente virtual com o comando: python -m venv venv
    3.1- Ative o ambiente virtual no Windows: .\venv\Scripts\activate
    3.2- Ative o ambiente virtual no Linux: source venv/bin/activate
    4- Instale as todas as dependências: pip install -r requirements.txt

# Passos para execução em ambiente de desenvolvimento

    1- Rode as migraçÕes com o comando: python manage.py migrate
    2- Para rodar a aplicação use o comando: python manage.py runserver
