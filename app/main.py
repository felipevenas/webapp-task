from flask import Flask
from interface.controller import main_bp, user_bp

app = Flask(__name__)
app.register_blueprint(main_bp)
app.register_blueprint(user_bp)