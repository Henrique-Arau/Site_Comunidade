Nesse site contém

* Alteração de usuários
* Login de usu[arios
* Criação de usuários
* Incluir Posts, Excluir posts e editar posts
* Filtra informações dentro de um Banco de dados
* Banco de dados usando flasks
* Lista de usuários
* Trabalha com imagens





>>> import secrets
>>> secrets.token_hex(16)



Criando as tabelas no Banco de dados

>>> from main import app

>>> from main import database
>>>
>>> from comunidadeImpressionadora import database

>>> database.create_all()
>>>
>>> from comunidadeImpressionadora.models import Usuario

>>> Usuario.query.all()
>>> 

Verificar usuario criado no banco de dados

>>> usuario = Usuario.query.first()

>>> usuario.email

>>> usuario.senha

>>> usuario.username

Verificar Post criado no banco de dados


>>> from comunidadeImpressionadora import database

>>> from comunidadeImpressionadora.models import Post

>>> post = Post.query.first()

>>> post.titulo

>>> post.corpo

