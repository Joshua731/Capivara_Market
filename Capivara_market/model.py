from Capivara_market.main import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuario(UserMixin, db.Model):
    __tablename__ = "Usuario"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    usuario = db.Column(db.String(150), nullable=False)

    senha = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
