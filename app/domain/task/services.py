from app.domain.task.repository_imp import TaskRepositoryImp

class TaskService():

    @staticmethod
    def create_task(form, user_id):

        data = {
            'titulo': form.titulo.data,
            'descricao': form.descricao.data,
            'status': form.status.data,
            'user_id': int(user_id)
        }

        return TaskRepositoryImp.create_task(data)
    
    @staticmethod
    def find_by_user(user_id: int):
        return TaskRepositoryImp.find_by_user(user_id)
    
    @staticmethod
    def find_by_id(task_id: int):
        return TaskRepositoryImp.find_by_id(task_id)
    
    @staticmethod
    def update_task(task_id: int, form, user_id: int):
        data = {
            'titulo': form.titulo.data,
            'descricao': form.descricao.data,
            'status': form.status.data,
            'user_id': user_id
        }

        return TaskRepositoryImp.update_task(task_id, data)
    
    @staticmethod
    def update_status(task_id: int) -> bool:
        return TaskRepositoryImp.done_task(task_id, 'Finalizada')

    @staticmethod 
    def delete_task(id):
        return TaskRepositoryImp.delete_task(id)