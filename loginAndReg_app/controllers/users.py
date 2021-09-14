from loginAndReg_app import app
from flask import render_template, redirect, request, session
from flask import flash

@app.route('/')
def home():
    return render_template('index.html')

    