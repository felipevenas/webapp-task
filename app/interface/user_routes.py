from flask import render_template, request, redirect, url_for, Blueprint, flash

from app.domain.user.services import UserService
from app.domain.user.model import User
from app.forms.forms import CadastroForm, LoginForm

user_bp = Blueprint("user_bp", __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register_page():

    form = CadastroForm()
    if form.validate_on_submit():
        user_data = User.to_dict(form)
        UserService.create(user_data)
        return redirect(url_for("user_bp.login_page"))
    
    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao cadastrar usuário: {err}", category="danger")
    return render_template("auth/register.html", form=form)

@user_bp.route('/login/auth', methods=['GET', 'POST'])
def login_page(): 
    form = LoginForm()
    # if form.validate_on_submit():
    # CORREÇÃO 1: Use os dados do formulário WTForms, é mais seguro.
    user_data = {
        "login": form.usuario.data,
        "senha": form.senha.data
    }

    authenticated_user = UserService.login(user_data)

    # CORREÇÃO 2: Verifique se o utilizador foi autenticado.
    if authenticated_user:
        flash(f"Bem-vindo de volta!", 'success')
        # CORREÇÃO 3: Redirecione para a página de tarefas.
        return redirect(url_for("user_bp.tasks_page"))
    else:
        flash("Utilizador ou senha inválidos.", 'danger')
        return redirect(url_for('user_bp.login_page'))
    


@user_bp.route('/tasks', methods=['GET'])
def tasks_page():
    return render_template("tasks.html")