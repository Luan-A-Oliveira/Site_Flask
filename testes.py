from main import app, database
from models import Usuario, Post


#criar database sempre criar app context antes da edição
#with app.app_context(): 
# database.create_all()

#editar database criar app context antes da edição
# with app.app_context():
#     usuario = Usuario(username='Luan', email='luan@email.com', senha='123456')
#     usuario2 = Usuario(username='Regina', email='regina@email.com', senha='123456')

#     database.session.add(usuario)
#     database.session.add(usuario2)

#     database.session.commit()


#consulta database
# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = meus_usuarios[0]
#     print(primeiro_usuario.username)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.posts)


#consulta no database por condição no exemplo consulta pelo id
# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.email)


