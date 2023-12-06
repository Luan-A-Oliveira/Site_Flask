from site_luan import app, database
# from site_luan.models import Usuario, Post


# criar database sempre criar app context antes da edição
with app.app_context():
    database.create_all()

# editar database criar app context antes da edição
# with app.app_context():
#     usuario = Usuario(username='Luan', email='luan@email.com', senha='123456')
#     usuario2 = Usuario(username='Regina', email='regina@email.com', senha='123456')

#     database.session.add(usuario)
#     database.session.add(usuario2)

#     database.session.commit()


# consulta database
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = meus_usuarios[0]
#     print(primeiro_usuario.username)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.posts)


# consulta no database por condição no exemplo consulta pelo id
# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.email)

# cria um post
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Primeiro post Luan',
#                     corpo='Luan deixa aqui sua mensagem')
#     database.session.add(meu_post)
#     database.session.commit()

# consulta o post
# with app.app_context():
#     post = Post.query.first()
#     print(post.autor.email)

#apaga todo databse e cria denovo
# with app.app_context():
#     database.drop_all()
#     database.create_all()
