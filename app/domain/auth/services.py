import requests

from app.infra.api_client import APIClient

class AuthService:

    # Os campos precisam estar exatamente iguais aos da API:

    @staticmethod
    def register(form):
        data = {
            "nome": form.nome.data,
            "email": form.email.data,
            "telefone": form.tel.data,
            "login": form.usuario.data,
            "senha": form.senha.data,
            "grupo": form.grupo.data,
            "setor": form.setor.data,
            "cargo": form.cargo.data,
            "ativo": form.ativo.data
        }

        try:
            api_response = APIClient.register(data)
            return api_response
        
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão com a API: {e}")
            return None
        
    @staticmethod
    def login(form):
        data = {
            "login": form.usuario.data,
            "senha": form.senha.data
        }
        try:
            api_response = APIClient.login(data)
            return api_response
        
        except requests.exceptions.HTTPError as e:
            print(f'Erro de conexão com a API: {e}')
            return None