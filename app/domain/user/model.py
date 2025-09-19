from dataclasses import dataclass
from flask import request

# Factory para criação de usuários:
@dataclass
class User():
        nome: str
        email: str
        login: str
        senha: str
        grupo: str
        telefone: str
        cargo: str
        setor: str
        ativo: str

        # Cria um objeto User a partir de um dicionário vindo da API:
        def from_dict(obj, data: dict) -> 'User':

                # Lógica de tradução do dicionário que vem da API:
                return obj(
                        id = data.get('id'),
                        nome = data.get('nome'),
                        login = data.get('login'),
                        telefone = data.get('telefone'),
                        email = data.get('email'),
                        cargo = data.get('cargo'),
                        ativo = data.get('ativo')
                        )
        
        def from_form(data: dict):
                return data == {
                        'nome': request.form.get('nome'),
                        'email': request.form.get('email'),
                        'telefone': request.form.get('telefone'),
                        'login': request.form.get('login'),
                        'senha': request.form.get('senha'),
                        'grupo': request.form.get('grupo'),
                        'setor': request.form.get('setor'),
                        'cargo': request.form.get('cargo'),
                        'ativo': request.form.get('ativo')
                        }
