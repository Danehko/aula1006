from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário',validators=[DataRequired("Campo obrigatorio")])
    password = PasswordField('Senha',validators=[DataRequired("Campo obrigatorio")])
    submit   = SubmitField("Entrar")