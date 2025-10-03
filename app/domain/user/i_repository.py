from abc import ABC, abstractmethod
from app.domain.user.model import User

class IUserRepository(ABC):

    @abstractmethod
    def get_all() -> list[User]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_login(user_login: str) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(user_id: int) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def create(user_data: dict) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def update(user_id: int, user_data: dict) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def delete(user_id: int) -> bool:
        raise NotImplementedError