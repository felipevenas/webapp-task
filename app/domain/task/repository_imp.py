from app.infra.api_client import APIClient
from app.domain.task.model import Task
from app.domain.task.i_repository import ITaskRepository

class TaskRepositoryImp(ITaskRepository):
    
    def create_task(self, data) -> Task:
        response = APIClient.create('/task', data)

        if response and response.status_code == 201:
            task_data = response.json()
            return Task.from_dict(task_data)
        return None
    
    def get_all():
        pass

    def get_by_user(self, user_id: int) -> list[Task]:
        api_response = APIClient.get_by_id(f'/tasks/user/{user_id}')

        if api_response:
            task_data_list = api_response.json()
            return [Task.from_dict(task_data) for task_data in task_data_list]
        return []
    
    def get_by_id(self, user_id: int) -> Task:
        response = APIClient.get_by_id(f'/task/{user_id}')

        if response:
            return response.json()
        return None
    
    def update_task(self, task_id: int, data):
        response = APIClient.update(f'/update/{task_id}', data)
        return response is not None and response.status_code == 200
            
    def update_status(self, task_id: int, data: dict):
        response = APIClient.update(f'/done/{task_id}', data)
        return response is not None and response.status_code == 200

    def delete_task(self, id: int) -> Task:
        api_response = APIClient.delete(f'/task/{id}')
        if api_response:
            return print(f'Tarefa excluída com sucesso!')