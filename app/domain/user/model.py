from dataclasses import dataclass

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

        @classmethod
        def from_dict(cls, data: dict) -> 'User':
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
        
        @classmethod
        def to_dict(cls, form):
                json = {
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
                return json
        
        @classmethod
        def login_to_dict(cls, form) -> dict:
                user_data = {
                        "login": form.usuario.data,
                        "senha": form.senha.data
                }
                return user_data
