from app.infra.api_client import APIClient
from app.domain.user.model import User
from app.domain.user.repository_imp import UserRepositoryImp

class UserService():
    
    @staticmethod
    def find_all() -> User:
        return UserRepositoryImp.find_all()

    @staticmethod
    def find_by_id(user_id: int) -> User | None:
        return UserRepositoryImp.find_by_id(user_id)
    
    @staticmethod
    def update(user_id: int, data: dict) -> User | None:
        return UserRepositoryImp.update(user_id, data)

    @staticmethod
    def delete(user_id: int) -> bool:
        return UserRepositoryImp.delete(user_id)
