from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    import datetime

    application = Flask(__name__)
    application.config.from_object(
        "config.DevelopmentConfig")

    db.init_app(application)

    from index.routes import index_blueprint
    application.register_blueprint(index_blueprint)

    from user.routes import blueprint_usuario
    application.register_blueprint(blueprint_usuario)

    from login.routes import login_blueprint
    application.register_blueprint(login_blueprint)

    from login import login_manager
    login_manager.init_app(application)

    if application.config["TESTING"]:
        with application.app_context():
            db.drop_all()
            db.create_all()

            # from util.crawler import get_data_from_rick_and_morty_apis
            # get_data_from_rick_and_morty_apis(db)

            db.session.add(Usuario(
                usuario="Joshian",
                senha="batata123"
            ))
            db.session.commit()

    return application


from Capivara_market.model import *

if __name__ == "__main__":
    application = create_app()
    print(application.url_map)
    application.run(host="0.0.0.0", port=5000)
