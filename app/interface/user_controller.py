from flask import render_template, request, redirect, url_for, Blueprint, flash
from app.domain.user.model import User
from app.domain.user.services import UserService
from app.infra.api_client import APIClient

user_bp = Blueprint("user_bp", __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        
        form_data = request.form.to_dict()
        created_user = UserService.create(form_data)

        if created_user:
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Erro ao cadastrar. Verifique os dados e tente novamente.', 'danger')
            return render_template('auth/register.html')
        
    return render_template('auth/register.html')