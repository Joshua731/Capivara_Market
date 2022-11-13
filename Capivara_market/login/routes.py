from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from Capivara_market.main import db
from . import login_blueprint
from .forms import LoginForm, RegisterForm
from Capivara_market.model import Usuario


@login_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index_blueprint.index"))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        usuario = str(login_form.usuario.data)
        user = Usuario.query.filter_by(usuario=usuario).first()
        if user is not None:
            if user.check_password(login_form.senha.data):
                login_user(user)
                return redirect(url_for("index_blueprint.index"))

        return "Usuário ou senha inválidos", 200

    return render_template("login/login.html", form=login_form)


@login_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index_blueprint.index"))


@login_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index_blueprint.index'))
    register_form = RegisterForm()

    if register_form.validate_on_submit():

        try:
            user = Usuario(
                usuario=register_form.usuario.data,
                senha=register_form.senha.data
            )
            user.set_password(register_form.senha.data)
            db.session.add(user)

            db.session.commit()

            return "Cadastro realizado com sucesso", 200

        except IntegrityError:
            db.session.rollback()
            return "E-mail já existente", 200

        except Exception as e:
            print(str(e))

    return render_template("login/register.html", form=register_form)
