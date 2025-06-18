from app import app
from flask import render_template
from app.forms.login_form import LoginForm
from app.controllers.authenticationController import AuthenticationController
from app.models  import Usuario
from app import db


@app.route("/")
def home():
    return render_template("index.html", usuario = None, usuario_logado = False)


@app.route("/sobre")
def sobre():
    return "Página Sobre"
@app.route("/contato")
def contato():
    return "Página de Contatos"


@app.route("/login", methods=['GET', 'POST'])
def login():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        return AuthenticationController.login(formulario)
    return render_template('login.html', title='Login', form = formulario)

@app.route("/dados", methods= ['GET', 'POST'])
def dados():
    usuario = Usuario(username='leosilva', email='leo@leo.com')
    db.session.add(usuario)
    db.session.commit()
    return render_template("index.html", usuario = None, usuario_logado = False)


@app.route("/inserir", methods=['GET', 'POST'])
def inserir():
    if request.methods == 'POST'
