from flask import Flask
from app.controller.main_controller import index_bp
from app.controller.auth.auth_controller import auth_bp
from app.controller.task_controller import task_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(index_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

