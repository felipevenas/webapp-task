from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import Length, Email, DataRequired

class CadastroForm(FlaskForm):
    nome = StringField(label='Nome:')
    usuario = StringField(label='Usuário:', validators=[Length(min=2, max=30), DataRequired()])
    senha = PasswordField(label='Senha:', validators=[Length(min=6, max=20), DataRequired()])
    email = EmailField(label='Email:', validators=[Email(), DataRequired()])
    tel = StringField(label='Telefone:', validators=[Length(max=11), DataRequired()])
    grupo = StringField(label='Grupo:')
    setor = StringField(label='Setor:')
    cargo = StringField(label='Cargo:')
    ativo = StringField(label='Ativo:', validators=[DataRequired()])
    submit = SubmitField(label='Cadastrar')

class LoginForm(FlaskForm):
    usuario = StringField(label='Usuário:', validators=[Length(min=6, max=20), DataRequired()])
    senha = PasswordField(label='Senha:', validators=[Length(min=6, max=20), DataRequired()])
    submit = SubmitField(label='Entrar')
