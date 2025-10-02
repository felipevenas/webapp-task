from app.infra.api_client import APIClient
from app.domain.task.model import Task
from app.domain.task.i_repository import ITaskRepository

class TaskRepositoryImp(ITaskRepository):
    
    @staticmethod
    def create_task(data) -> Task:
        response = APIClient.create('/task', data)

        if response and response.status_code == 201:
            task_data = response.json()
            return Task.from_dict(task_data)
        return None
    
    @staticmethod
    def get_by_user(user_id: int) -> list[Task]:
        api_response = APIClient.get_by_id(f'/tasks/user/{user_id}')

        if api_response:
            task_data_list = api_response.json()
            return [Task.from_dict(task_data) for task_data in task_data_list]
        return []
    
    @staticmethod
    def get_by_id(user_id: int) -> Task:
        response = APIClient.get_by_id(f'/task/{user_id}')

        if response:
            return response.json()
        return None
    
    @staticmethod
    def update_task(task_id: int, data):
        response = APIClient.update(f'/update/{task_id}', data)
        return response is not None and response.status_code == 200
            
    @staticmethod
    def update_status(task_id: int, data: dict):
        response = APIClient.update(f'/done/{task_id}', data)
        return response is not None and response.status_code == 200

    @staticmethod
    def delete_task(id: int) -> Task:
        api_response = APIClient.delete(f'/task/{id}')
        if api_response:
            return print(f'Tarefa excluída com sucesso!')