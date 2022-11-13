from flask import render_template

from . import blueprint_usuario
from .forms import UserForm
from Capivara_market.main import db

from Capivara_market.model import Usuario


@blueprint_usuario.route("/", methods=["GET"])
def list_users():
    return render_template(
        template_name_or_list="user/list.html",
        users=Usuario.query.all())


@blueprint_usuario.route("/new", methods=["GET", "POST"])
def new_user():
    form = UserForm()

    if form.validate_on_submit():
        user = Usuario(id=int(form.id.data), usuario=str(form.usuario.data))
        db.session.add(user)
        db.session.commit()
        return "Usuario inserido com sucesso", 200

    return render_template("user/new.html", form=form)
