from flask import render_template, request, redirect, session, flash, url_for
from spe import app, db
from models import ALUNO, PROFESSOR

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    pass

@app.route('/authenticate', methods=['POST', ])
def authenticate():
    pass

@app.route('/logout')
def logout():
    pass