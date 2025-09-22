from dataclasses import dataclass
from flask import request

# Factory para criação de usuários:
@dataclass
class User():
        id: int
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
        @classmethod
        def from_dict(cls, data: dict) -> 'User':
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
                # Lógica de tradução do dicionário que vem da API:
                return cls(
                        id = data.get('id'),
                        nome = data.get('nome'),
<<<<<<< Updated upstream
                        login = data.get('login'),
=======
                        login = data.get('usuario'),
>>>>>>> Stashed changes
                        senha = data.get('senha'),
                        telefone = data.get('telefone'),
                        email = data.get('email'),
                        cargo = data.get('cargo'),
                        grupo = data.get('grupo'),
                        setor = data.get('setor'),
                        ativo = data.get('ativo')
                        )
<<<<<<< Updated upstream
=======
        
        @classmethod
        def to_dict(cls, form) -> dict:
                user_data = {
                        "nome": form.nome.data,
                        "login": form.usuario.data,
                        "senha": form.senha.data,
                        "email": form.email.data,
                        "telefone": form.tel.data,
                        "grupo": form.grupo.data,
                        "setor": form.setor.data,
                        "cargo": form.cargo.data,
                        "ativo": form.ativo.data
                }
                return user_data
>>>>>>> Stashed changes
