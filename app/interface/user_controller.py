from flask import render_template, request, redirect, url_for, Blueprint, flash
from app.domain.user.services import UserService

user_bp = Blueprint("user_bp", __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        form_data = request.form.to_dict()
        created_user = UserService.create(form_data)

        if created_user:
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('user_bp.login'))
        else:
            flash('Erro ao cadastrar. Verifique os dados e tente novamente.', 'danger')
            return render_template('auth/register.html')
        
    return render_template('auth/register.html')

@user_bp.route('/login')
def login():
    return render_template('auth/login.html')
