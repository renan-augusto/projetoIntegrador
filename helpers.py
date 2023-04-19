import os
from spe import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField


def UserForm(FlaskForm):
    email = StringField('E-mail', [validators.data_required(), validators.Length(min=1, max=50)])
    pwd = PasswordField('Senha', [validators.data_required(), validators.Length(min=1, max=100)])
    login = SubmitField('login')