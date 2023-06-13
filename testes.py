from main import app, database
from models import Usuario, Post


# with app.app_context():
#    database.create_all()

#with app.app_context():
#    database.create_all()
#    usuario = Usuario(username="Henrique", email="henrique@gmail.com", senha="151246")
#    usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha="159123")
#    database.session.add(Usuario)
#    database.session.add(usuario2)
#    database.session.commit()

#with app.app_context():
#    meus_usuarios = Usuario.query.all()
#    print(meus_usuarios)
#    primeiro_usuario = Usuario.query.first()
#    print(primeiro_usuario.id)
#    print(primeiro_usuario.email)
#    print(primeiro_usuario.posts)


# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste)


# with app.app_context():
#     database.create_all()
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post do Lira", corpo="Lira voando")
#     database.session.add(meu_post)
#     database.session.commit()

with app.app_context():
    post = Post.query.first()
    print(post.titulo)
    print(post.autor)
    print(post.id)