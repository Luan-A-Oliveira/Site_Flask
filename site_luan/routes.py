from flask import render_template, redirect, url_for, flash, request
from site_luan import app, database, bcrypt
from site_luan.forms import FormLogin, FormCadastro
from site_luan.models import Usuario

lista_usuarios = ['luan', 'regina', 'aurora', 'neguinho', 'gedi']


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_cadastro = FormCadastro()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(
            f'Login feito com sucesso para o email: {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_cadastro.validate_on_submit() and 'botao_submit_criar' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_cadastro.senha.data)
        usuario = Usuario(username=form_cadastro.username.data,
                          email=form_cadastro.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit
        flash(
            f'Conta criada para o email: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_cadastro=form_cadastro)
