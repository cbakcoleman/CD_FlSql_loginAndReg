from loginAndReg_app import app
from flask import render_template, redirect, request, session
from flask import flash
from loginAndReg_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['post'])
def add_user():
    if not User.validate_user(request.form):
        return redirect('/')

    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : password_hash
    }

    User.add_user(data)
    return redirect('/success')

@app.route('login', methods=['post'])
def login():
    data = { "email" : request.form["email"] }
    valid_user = User.get_by_email(data)
    if not valid_user:
        flash('Invalid Email or Password')
        

@app.route('/success')
def success():
    #ind_user = User.get_user({"id" : id })
    return render_template('success.html')