from abc import ABC, abstractmethod
from app.domain.user.model import User

class IUserRepository(ABC):

    @abstractmethod
    def get_all() -> list[User]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(user_id: int) -> User:
        raise NotImplementedError
    
    @abstractmethod
    def create(data: dict) -> User:
        raise NotImplementedError