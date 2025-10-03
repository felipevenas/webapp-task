from app.domain.task.repository_imp import TaskRepositoryImp

class TaskService():

    def __init__(self, repository: TaskRepositoryImp):
        self.repository = repository

    def create_task(self, form, user_id):

        data = {
            'titulo': form.titulo.data,
            'descricao': form.descricao.data,
            'status': form.status.data,
            'user_id': int(user_id)
        }

        return self.repository.create_task(data)
    
    def get_by_user(self, user_id: int):
        return self.repository.get_by_user(user_id)
    
    def get_by_id(self, task_id: int):
        return self.repository.get_by_id(task_id)
    
    def update_task(self, task_id: int, form, user_id: int):
        data = {
            'titulo': form.titulo.data,
            'descricao': form.descricao.data,
            'status': form.status.data,
            'user_id': user_id
        }

        return self.repository.update_task(task_id, data)
    
    def update_status(self, task_id: int) -> bool:
        data = {
            'status': 'Finalizada'
        }
        return self.repository.update_status(task_id, data)

    def delete_task(self, id):
        return self.repository.delete_task(id)