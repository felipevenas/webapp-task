from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return render_template('home.html')

@main_bp.route('/login')
def login():
    return render_template('auth/login.html')

@main_bp.route('/register')
def register():
    return render_template('auth/register.html')

