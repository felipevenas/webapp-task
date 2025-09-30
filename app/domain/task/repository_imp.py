from app.infra.api_client import APIClient
from app.domain.task.model import Task
from app.domain.task.i_repository import ITaskRepository

class TaskRepositoryImp(ITaskRepository):
    
    @staticmethod
    def create_task(data) -> Task:
        response = APIClient.create_task(data)

        if response and response.status_code == 201:
            task_data = response.json()
            return Task.from_dict(task_data)
        return None
    
    @staticmethod
    def find_by_user(user_id: int) -> list[Task]:
        api_response = APIClient.find_by_user(user_id)

        if api_response:

            task_data_list = api_response.json()

            return [Task.from_dict(task_data) for task_data in task_data_list]
        return []
    
    @staticmethod
    def delete_task(id: int) -> Task:
        api_response = APIClient.delete_task(id)
        
        if api_response:
            return print(f'Tarefa excluída com sucesso!')
        