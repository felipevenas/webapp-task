from flask import Blueprint, render_template
from app.forms.forms import LoginForm, CadastroForm

index_bp = Blueprint('index_bp', __name__)

@index_bp.route('/')
def index_page():
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

@index_bp.route('/how-to-use')
def how_to_use_page():
    return render_template('how_to_use.html')