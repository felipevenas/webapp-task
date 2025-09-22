<<<<<<< Updated upstream
from flask import Flask
from .interface.controller import main_bp
from .interface.user_controller import user_bp

app = Flask(__name__)
app.secret_key = 'tst'
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)
=======
<<<<<<< Updated upstream
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('auth/register.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')
=======
from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
import os

from app.interface.routes import main_bp
from app.interface.user_routes import user_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)
>>>>>>> Stashed changes
>>>>>>> Stashed changes
