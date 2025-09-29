from flask import render_template, request, redirect, url_for, Blueprint, flash

from app.domain.user.services import UserService
from app.domain.user.model import User
from app.forms.forms import CadastroForm, LoginForm

user_bp = Blueprint("user_bp", __name__)
    
@user_bp.route('/tasks')
def tasks_page():
    return render_template("tasks.html")