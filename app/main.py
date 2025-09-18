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