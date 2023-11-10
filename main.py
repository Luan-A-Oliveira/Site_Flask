from flask import Flask, render_template, url_for
from forms import FormLogin, FormCadastro 

app = Flask(__name__)

lista_usuarios = ['luan', 'regina', 'aurora', 'neguinho', 'gedi']

app.config['SECRET_KEY']= '01a4aa9f9065cc494ef564c3f114a1b8'

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login")
def login():
    form_login = FormLogin()
    form_cadastro = FormCadastro()    
    return render_template('login.html', form_login=form_login, form_cadastro=form_cadastro)


if __name__ == '__main__':
    app.run(debug=True)
