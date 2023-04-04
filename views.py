from flask import render_template, request, redirectm, session, flash, url_for
from spe import app, db
from models import ALUNO, PROFESSOR

@app.route('/')
def index():
    return render_template('index.html')