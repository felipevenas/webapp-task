from abc import ABC, abstractmethod
from app.domain.task.model import Task

class ITaskRepository(ABC):

    @abstractmethod
    def find_all() -> list[Task]:
        raise NotImplementedError
    
    @abstractmethod
    def find_by_id(task_id: int) -> Task:
        raise NotImplementedError
    
    @abstractmethod
    def create(data: dict) -> Task:
        raise NotImplementedError
    