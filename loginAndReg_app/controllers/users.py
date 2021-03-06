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

    user_id = User.add_user(data)
    session['user_id'] = user_id

    return redirect(f'/success/{user_id}')

@app.route('/login', methods=['post'])
def login():
    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)

    if not user:
        flash('Invalid login entry!', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid login entry!', 'login')
        return redirect('/')

    session['user_id'] = user.id

    return redirect(f'/success/{session["user_id"]}')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/success/<id>')
def success(id):
    if not session['user_id']:
        return redirect('/')
    user = User.get_by_id({'id' :id}) 
    return render_template('success.html', user = user)

