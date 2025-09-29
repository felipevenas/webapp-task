from flask import Flask
from app.interface.controller import index_bp
from app.interface.user_controller import user_bp
from app.interface.auth.auth_controller import auth_bp
from app.interface.task_controller import task_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(index_bp)
app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

