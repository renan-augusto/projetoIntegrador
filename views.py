from flask import render_template, request, redirect, session, flash, url_for
from spe import app, db
from models import ADMIN    

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/register-student', methods=['POST','GET', ])
def register_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        ra = request.form['ra'] 
        pwd = request.form['pwd']
        
        student = ALUNO(name, email, ra, pwd)
        db.session.add(student)
        db.session.commit()
     
    return render_template('register-student.html')

