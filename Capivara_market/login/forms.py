from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    usuario = StringField("Usuário", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    submit = SubmitField("Logar")


class RegisterForm(FlaskForm):
    usuario = StringField("Nome", validators=[DataRequired()])
    senha = PasswordField("Senha", validators=[
        DataRequired(),
        EqualTo("confirma", message="Senhas devem ser compatíveis")])
    confirma = PasswordField("Confirmação")
    submit = SubmitField("Cadastrar")
