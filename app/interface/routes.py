from flask import Blueprint, render_template
from app.forms.forms import LoginForm, CadastroForm

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@main_bp.route('/register')
def register():
    form = CadastroForm()
    return render_template('auth/register.html', form=form)