from flask import Blueprint, render_template, session, redirect, url_for, flash

from app.domain.task.repository_imp import TaskRepositoryImp
from app.forms.forms import LoginForm, CadastroForm, CreateTaskForm
from app.domain.task.services import TaskService

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index_page():
    if session['login'] == None or 'login' not in session:
        return redirect(url_for('index_bp.login_page'))
    
    return render_template('home.html')

@index_bp.route('/login')
def login_page():
    form = LoginForm()
    return render_template('auth/login_page.html',
                           form=form)

@index_bp.route('/register')
def register_page():
    form = CadastroForm()
    return render_template('auth/register_page.html', 
                           form=form)

@index_bp.route('/task/<int:id>')
def update_page(id):
    if session['login'] == None or 'login' not in session:
        flash('É necessário se autenticar!')
        return redirect(url_for('index_bp.login_page'))

    repository = TaskRepositoryImp()
    service = TaskService(repository)

    get_task = service.get_by_id(id)

    if not get_task:
        flash('Nenhuma tarefa foi encontrada!')
        return redirect(url_for('index_bp.tasks_page'))
    
    form = CreateTaskForm()

    form.titulo.data = get_task['titulo']
    form.descricao.data = get_task['descricao'] 

    return render_template('task/update_task.html',
                           form=form,
                           id=id)

@index_bp.route('/tasks')
def tasks_page():
    if 'user_id' not in session:
        flash('É necessário se autenticar!')
        return redirect(url_for('index_bp.login_page'))
    
    user_id = session.get('user_id')

    repository = TaskRepositoryImp()
    service = TaskService(repository)

    tasks = service.get_by_user(user_id)

    return render_template('task/tasks.html',
                           tasks=tasks)

@index_bp.route('/task')
def create_task_page():
    form = CreateTaskForm()
    if session['login'] == None or 'login' not in session:
        flash('É necessário se autenticar!')
        return redirect(url_for('index_bp.login_page'))

    return render_template('task/create_task.html',
                           form=form)