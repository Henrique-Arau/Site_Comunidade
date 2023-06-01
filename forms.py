from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class FormCriarConta():
    username = StringField('Nome de usuário')
    email = StringField('E-mail')
    senha = PasswordField('Senha')
    confirmacao = PasswordField('Confirmação da senha')
    botao_submit_criarconta = SubmitField('Criar Conta')