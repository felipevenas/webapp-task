from flask import Blueprint, redirect, url_for, request, flash, session

from app.forms.forms import CreateTaskForm
from app.domain.task.services import TaskService
from app.domain.task.repository_imp import TaskRepositoryImp

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/task', methods=['POST'])
def create_task():

    form = CreateTaskForm(request.form)
    
    repository = TaskRepositoryImp()
    service = TaskService(repository)

    if form.validate_on_submit():

        if session ['login'] == None or 'login' not in session:
            return redirect(url_for('index_bp.login_page'))

        user_id = session.get('user_id')
        service.create_task(form, user_id)

        if user_id:
            flash('Tarefa adicionada com sucesso!', category='sucess')
            return redirect(url_for("index_bp.tasks_page"))
        else:
            flash('Não foi possível adicionar a tarefa. Tente novamente!', category='danger')   
            return redirect(url_for('index_bp.tasks_page'))
        
    else:
        flash('Houve um problema no formulário. Tente novamente!', category='danger') # <-- Sempre está caindo aqui!
        return redirect(url_for('index_bp.tasks_page'))

@task_bp.route('/delete/<int:task_id>')
def delete_task(task_id):
    if session ['login'] == None or 'login' not in session:
        return redirect(url_for('index_bp.login_page'))
    
    repository = TaskRepositoryImp()
    service = TaskService(repository)

    get_task = service.get_by_id(task_id)
    
    if get_task:
        service.delete_task(task_id)
        flash('Tarefa deletada com sucesso!')
        return redirect(url_for('index_bp.tasks_page'))
    
    else:
        flash('Não foi possível excluir a tarefa!')
        return redirect(url_for('index_bp.tasks_page'))
    
@task_bp.route('/update', methods=['POST'])
def update_task():

    if session ['login'] == None or 'login' not in session:
        return redirect(url_for('index_bp.login_page'))

    repository = TaskRepositoryImp()
    service = TaskService(repository)

    user_id = session.get('user_id')
    form = CreateTaskForm(request.form)

    if form.validate_on_submit():

        task_id = request.form.get('inputId')

        print(task_id)

        service.get_by_id(task_id)
        updated_task = service.update_task(task_id, form, user_id)

        if updated_task:
            flash('Tarefa editada com sucesso!')
            return redirect(url_for('index_bp.tasks_page'))
        else:
            flash('Não foi possível editar a tarefa!')
            return redirect(url_for('index_bp.update_page'))
            
@task_bp.route('/done/<int:task_id>')
def done_task(task_id):

    if session['login'] == None or 'login' not in session:
        flash('É necessário se autenticar!')
        return redirect(url_for('index_bp.login_page'))
    
    repository = TaskRepositoryImp()
    service = TaskService(repository)

    sucess = service.update_status(task_id)

    if sucess:
        flash('Tarefa finalizada!')
        return redirect(url_for('index_bp.tasks_page'))   
    else: 
        flash('Não foi possível atualizar o status da tarefa!')
        return redirect(url_for('index_bp.tasks_page'))   