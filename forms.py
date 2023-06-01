from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class FormCriarConta(FlaskForm):
    username = StringField('Nome de usuário')
    email = StringField('E-mail')
    senha = PasswordField('Senha')
    confirmacao = PasswordField('Confirmação da senha')
    botao_submit_criarconta = SubmitField('Criar Conta')


class FormLogin(FlaskForm):
    email = StringField('E-mail')
    senha = PasswordField('Senha')
    botao_submit_criarconta = SubmitField('Fazer Login')