from flask import Blueprint, redirect, url_for, request, flash, session

from app.forms.forms import CreateTaskForm
from app.domain.task.services import TaskService

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/task', methods=['POST'])
def create_task():

    form = CreateTaskForm(request.form)

    if form.validate_on_submit():

        if session ['login'] == None or 'login' not in session:
            return redirect(url_for('index_bp.login_page'))

        user_id = session.get('user_id')
        TaskService.create_task(form, user_id)

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
    
    find_task = TaskService.find_by_id(task_id)
    
    if find_task:
        TaskService.delete_task(task_id)
        flash('Tarefa deletada com sucesso!')
        return redirect(url_for('index_bp.tasks_page'))
    
    else:
        flash('Não foi possível excluir a tarefa!')
        return redirect(url_for('index_bp.tasks_page'))
    
@task_bp.route('/update', methods=['POST'])
def update_task():

    if session ['login'] == None or 'login' not in session:
        return redirect(url_for('index_bp.login_page'))

    user_id = session.get('user_id')

    form = CreateTaskForm(request.form)

    if form.validate_on_submit():

        task_id = request.form.get('inputId')

        task = TaskService.find_by_id(request.form['inputId'])
        TaskService.update_task(task_id, form, user_id)

        if task:
            flash('Tarefa editada com sucesso!')
            return redirect(url_for('index_bp.tasks_page'))
        else:
            flash('Não foi possível editar a tarefa!')
            redirect(url_for('index_bp.update_page'))
            
@task_bp.route('/done/<int:task_id>')
def done_task(task_id):

    if session['login'] == None or 'login' not in session:
        flash('É necessário se autenticar!')
        return redirect(url_for('index_bp.login_page'))

    sucess = TaskService.update_status(task_id)

    if sucess:
        flash('Tarefa finalizada!')
        return redirect(url_for('index_bp.tasks_page'))   
    else: 
        flash('Não foi possível atualizar o status da tarefa!')
        return redirect(url_for('index_bp.tasks_page'))   