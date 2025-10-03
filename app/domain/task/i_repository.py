from abc import ABC, abstractmethod
from app.domain.task.model import Task

class ITaskRepository(ABC):

    @abstractmethod
    def get_all() -> list[Task]:
        pass
    
    @abstractmethod
    def get_by_id(self, task_id: int) -> Task:
        pass
    
    @abstractmethod
    def create_task(self, data: dict) -> Task:
        pass
    
    @abstractmethod
    def update_task(self, task_id: int, data: dict):
        pass

    @abstractmethod
    def update_status(self, task_id: int, data: dict):
        pass

    @abstractmethod
    def delete_task(self, id: int):
        pass
    