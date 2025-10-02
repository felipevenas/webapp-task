from app.infra.api_client import APIClient, API_URL
from app.domain.auth.i_repository import IAuthRepository
from app.domain.user.model import User

class AuthRepositoryImp(IAuthRepository):

    def login(self, credentials: dict) -> User | None:
        response = APIClient.login(credentials)
        if response:
            user_data = response.json()
            return User.from_dict(user_data)
        return None
    
    def register(self, credentials: dict) -> User | None:
        response = APIClient.register('/create', credentials)
        if response:
            user_data = response.json()
            return User.from_dict(user_data) # Fábrica de usuários.
        return None