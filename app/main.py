from flask import Flask
from app.interface.routes import main_bp
from app.interface.user_routes import user_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)

