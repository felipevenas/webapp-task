from flask import render_template, request, redirect, url_for, flash, Blueprint
from app.infra.api_client import APIClient

user_bp = Blueprint("user_bp", __name__)

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Se o formulário for enviado (método POST)
    if request.method == 'POST':

        # 1. Coletar dados do formulário
        user_data = {
            "nome": request.form.get('nome'),
            "email": request.form.get('email'),
            "senha": request.form.get('senha'),
            "login": request.form.get('login'),
            "grupo": request.form.get('grupo'),
            "telefone": request.form.get('telefone'),
            "cargo": request.form.get('cargo'),
            "setor": request.form.get('setor'),
            "ativo": request.form.get('ativo')
        }

        # 2. Chamar a API para criar o usuário
        response_data = APIClient.post('user', data=user_data)

        # 3. Tratar a resposta
        if response_data:
            print('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))
        else:
            print('Erro ao cadastrar. Verifique os dados e tente novamente.', 'danger')
            return render_template('auth/register.html')

    # Se a requisição for GET, apenas mostra a página
    return render_template('auth/register.html')