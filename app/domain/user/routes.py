from flask import render_template, request, redirect, url_for, flash
from app.main import app
from app.domain.user.services import UserService
from app.infra.api_client import APIClient

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Coleta os dados do formulário
        user_data = {
            "nome_completo": request.form.get('nome_completo'),
            "email": request.form.get('email'),
            "telefone": request.form.get('telefone'),
            "usuario": request.form.get('usuario'),
            "senha": request.form.get('senha'),
            # Adicione outros campos conforme necessário
        }

        # 2. Use sua classe para fazer a chamada POST
        # O endpoint é apenas a parte final da URL, ex: "users/"
        response_data = APIClient.post('users/', data=user_data)

        # 3. Verifique a resposta
        # Sua classe retorna None em caso de erro de comunicação
        if response_data:
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for('login'))
        else:
            # A mensagem de erro específica foi impressa no console pela sua classe
            flash('Ocorreu um erro ao realizar o cadastro. Tente novamente.', 'danger')
            
    return render_template('register.html')