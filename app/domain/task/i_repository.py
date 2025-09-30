from abc import ABC, abstractmethod
from app.domain.task.model import Task

class ITaskRepository(ABC):

    @abstractmethod
    def get_all() -> list[Task]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(task_id: int) -> Task:
        raise NotImplementedError
    
    @abstractmethod
    def create(data: dict) -> Task:
        raise NotImplementedError