from flask_login import LoginManager

from Capivara_market.model import Usuario

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return Usuario.query.get(user_id)
