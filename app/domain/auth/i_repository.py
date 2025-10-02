from abc import ABC, abstractmethod

class IAuthRepository(ABC):

    @abstractmethod
    def login(data: dict) -> dict:
        pass

    @abstractmethod
    def register(data: dict) -> dict:
        pass