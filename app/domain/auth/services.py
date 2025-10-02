from app.domain.auth.repository_imp import AuthRepositoryImp

class AuthService:

    def __init__(self):
        self.repository = AuthRepositoryImp()

    def register(self, form):
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
        return self.repository.register(data)
        
    def login(self, form):
        data = {
            "login": form.usuario.data,
            "senha": form.senha.data
        }
        return self.repository.login(data) # <- Está acusando como se fosse dois argumentos que estou passando aquoi.