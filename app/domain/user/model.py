from dataclasses import dataclass

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
                        email = data.get('email'),
                        ativo = data.get('ativo')
                        )
