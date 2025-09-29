from app.infra.api_client import APIClient
from app.domain.task.model import Task
from app.domain.task.i_repository import ITaskRepository

class TaskRepositoryImp(ITaskRepository):
    @staticmethod
    def create_task(data) -> Task:
        task_data = APIClient.create_task('/task', data)
        if task_data:
            return Task.from_dict(task_data)
        return None