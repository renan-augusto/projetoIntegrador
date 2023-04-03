from flask import Flask, render_template, request, redirectm, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'grupo1sjrp'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}: // {usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost', 
        database = 'REGISTRO_ALUNOS_FAMERP'
    )

db = SQLAlchemy(app) 
   
@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)