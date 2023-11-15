from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCadastro
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['luan', 'regina', 'aurora', 'neguinho', 'gedi']

app.config['SECRET_KEY']= '01a4aa9f9065cc494ef564c3f114a1b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

database = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')

@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route("/login", methods=['GET', 'POST'] )
def login():
    form_login = FormLogin()
    form_cadastro = FormCadastro()  
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso para o email: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_cadastro.validate_on_submit() and 'botao_submit_criar' in request.form:
        flash(f'Conta criada para o email: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_cadastro=form_cadastro)


if __name__ == '__main__':
    app.run(debug=True)
