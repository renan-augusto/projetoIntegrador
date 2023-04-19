from spe import app
from flask import render_template, request, redirect, session, flash, url_for
from models import USUARIO
from flask_bcrypt import check_password_hash
from helpers import UserForm

@app.route('/')
def index():
    advance = advance.args.get('advance')
    form = UserForm()
    return render_template('index.html', advance=advance, form=form)

@app.route('/auth', methods=['POST', ])
def auth():
    form = UserForm(request.form)
    user = USUARIO.query.filter_by(email=form.email.data).first()
    pwd = check_password_hash(USUARIO.SENHA, form.pwd.data)
    
    if user and pwd:
        session['logged_user'] = USUARIO.NOME
        flash(USUARIO.NOME + ' logado com sucesso')
        advance_page = request.form['advance']
        return redirect(advance_page)
    else:
        flash('Usuário não logado!')
        return redirect(url_for('/'))
    
    
@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com susceso')
    return redirect(url_for('index'))