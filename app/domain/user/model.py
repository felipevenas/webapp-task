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

                # Lógica de tradução do dicionário que vem da API:
                return cls(
                        id = data.get('id'),
                        nome = data.get('nome'),
                        login = data.get('login'),
                        senha = data.get('senha'),
                        telefone = data.get('telefone'),
                        email = data.get('email'),
                        cargo = data.get('cargo'),
                        grupo = data.get('grupo'),
                        setor = data.get('setor'),
                        ativo = data.get('ativo')
                        )
