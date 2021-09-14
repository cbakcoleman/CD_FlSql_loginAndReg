from loginAndReg_app import app
from flask import render_template, redirect, request, session
from flask import flash
from loginAndReg_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('register_user', methods=['post'])
def add_user():
    if not User.validate_user(request.form):
        return redirect('/')
    User.add_user(request.form)
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')