from flask import Blueprint

blueprint_usuario = Blueprint(
    "blueprint_usuario", __name__, url_prefix="/user")

from .routes import *
