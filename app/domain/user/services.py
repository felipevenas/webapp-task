from app.domain.user.model import User
from app.domain.user.repository_imp import UserRepositoryImp

class UserService():
    
    @staticmethod
    def get_all() -> User:
        return UserRepositoryImp.get_all()

    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        return UserRepositoryImp.get_by_id(user_id)
    
    @staticmethod
    def update(user_id: int, data: dict) -> User | None:
        return UserRepositoryImp.update(user_id, data)

    @staticmethod
    def delete(user_id: int) -> bool:
        return UserRepositoryImp.delete(user_id)
    