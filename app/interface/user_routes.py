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

@user_bp.route('/user/login', methods=['GET', 'POST'])
def login_page():

    form = LoginForm()
    if form.validate_on_submit():
        credentials = User.to_dict(form)
        UserService.login(credentials)
        redirect(url_for("user_bp.tasks_page"))

    if form.errors != {}:
        for err in form.errors.values():
            flash(f"Erro ao fazer login: {err}", category="danger")
    return render_template("auth/login.html", form=form)
    
@user_bp.route('/', methods=['GET'])
def tasks_page():
    return render_template("tasks.html")