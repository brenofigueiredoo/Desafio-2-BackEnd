
# Sobre o projeto

Nesse projeto foi desenvolvido uma interface web que aceita upload do arquivo CNAB, com os dados das movimentações financeiras de várias lojas. A aplicação faz a tratativa dos dados e armazena-os em um banco de dados relacional e exibe essas informaçes em tela.

# Funcionalidades

Na rota http://127.0.0.1:8000/ é onde fica a possibilidade de fazer o upload do arquivo CNAB.txt. A aplicação só funcionará corretamente se o arquivo for do tipo CNAB.txt.

Logo após clicar no botão "enviar" junto ao arquivo CNAB, o usuário será transferido à rota http://127.0.0.1:8000/api/transacoes/ onde trás os resultados da aplicação.

# Tecnologias utilizadas

- Python 3.11.1
- Django RestFramework
- SQLite

# Passos de instalação

1- Clone o repositório para a sua máquina


2- Crie um ambiente virtual com o comando:
```
python -m venv venv
```

3- Ative o ambiente virtual: 
```
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

4- Instale todas as dependências: 
```
pip install -r requirements.txt
```

# Passos para execução em ambiente de desenvolvimento

1- Rode as migrações com o comando:
```
python manage.py migrate
```

2- Para rodar a aplicação use o comando:
```
python manage.py runserver
```
