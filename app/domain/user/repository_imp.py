from app.infra.api_client import APIClient
from app.domain.user.model import User
from app.domain.user.i_repository import IUserRepository

class UserRepositoryImp(IUserRepository):

    @staticmethod
    def find_all() -> list[User]:
        users_data = APIClient.get_users("/users")
        if users_data:
            return [User.from_dict(users_data) for user_data in users_data]
        return []
    
    @staticmethod
    def find_by_login(user_login: str) -> User:
        user_data = APIClient.find_by_login(f'user/{user_login}')
        if user_data:
            return User.from_dict(user_data)
        return None

    @staticmethod
    def update(user_id: int, user_data: dict) -> User:
        updated_data = APIClient.put(f"/user/{user_id}", data=user_data)
        if updated_data:
            return User.from_dict(updated_data)
        return None

    @staticmethod
    def delete(user_id: int) -> bool:
        response = APIClient.delete(f"/user/{user_id}")
        return response is not None
    
    @staticmethod   
    def find_by_id(user_id: int) -> User | None:
        user_data = APIClient.get(f"/user/{user_id}")
        if user_data:
            return User.from_dict(user_data)
        return None
    
    @staticmethod
    def create(user_data: dict) -> User:
        user_data = APIClient.post("/user", data=user_data)
        if user_data:
            return User.from_dict(user_data)
        return None 
    
    @staticmethod
    def login(credentials: dict) -> dict | None:
        credentials = APIClient.login(f"/user/login", data=credentials)
        if credentials:
            return User.login_to_dict(credentials)
        return None
 
            