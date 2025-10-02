from flask import Blueprint, flash, redirect, url_for, request, session

from app.forms.forms import CadastroForm, LoginForm 
from app.domain.auth.services import AuthService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():

    form = CadastroForm(request.form) 
    service = AuthService()

    if form.validate_on_submit():
        response = service.register(form)
        
        if response:
            flash('Usuário cadastrado com sucesso!', category='sucess')
            return redirect(url_for("index_bp.login_page"))
        else:
            flash('Não foi possível realizar o cadastro!', category='danger')   
            return redirect(url_for('index_bp.login_page'))

@auth_bp.route('/auth', methods=['POST'])
def login(): 

    form = LoginForm(request.form)
    service = AuthService()

    authenticated_user = service.login(form) 

    if authenticated_user:
        
        flash(f"Bem-vindo de volta {form.usuario.data}!", 'success')

        session['login'] = authenticated_user.login
        session['user_id'] = authenticated_user.id

        return redirect(url_for("index_bp.tasks_page"))

    else:
        flash("Utilizador ou senha inválidos.")
        return redirect(url_for('index_bp.login_page'))
    
@auth_bp.route('/logout')
def logout():
    session['login'] = None
    flash('Usuário deslogado!')
    return redirect(url_for('index_bp.login_page'))