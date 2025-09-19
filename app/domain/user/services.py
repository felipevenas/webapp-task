from app.infra.api_client import APIClient
from app.domain.user.model import User
from app.domain.user.repository_imp import UserIRepository as repository

class UserService():
    
    @staticmethod
    def find_all() -> User:
        data = repository.find_all

    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        data = APIClient.get(f"/user/{user_id}")

        if data:
            return User.from_dict(data)
        
        return None