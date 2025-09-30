from app.domain.task.repository_imp import TaskRepositoryImp

class TaskService():

    @staticmethod
    def create_task(form, user_id):

        data = {
            'titulo': form.titulo.data,
            'descricao': form.descricao.data,
            'user_id': int(user_id)
        }

        return TaskRepositoryImp.create_task(data)
    
    @staticmethod
    def find_by_user(user_id: int):
        return TaskRepositoryImp.find_by_user(user_id)
    
    @staticmethod 
    def delete_task(id):
        return TaskRepositoryImp.delete_task(id)