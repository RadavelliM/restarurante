from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..db_connexion import get_db_connection

auth_bp = Blueprint("auth", __name__, url_prefix='')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')

    email = request.form.get('email')
    senha = request.form.get('senha')

    if not email or not senha:
        flash("Informe todos os campos", "erro")
        return redirect(url_for('auth.login'))

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM Usuarios WHERE Usuario_email = %s AND Usuario_senha = %s"
    cursor.execute(sql, (email, senha))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        flash("Email ou senha incorretos", "erro")
        return redirect(url_for('auth.login'))

    session['logado'] = True
    session['tipo'] = user['Usuario_tipo']

    if user['Usuario_tipo'] == 0:
        return redirect(url_for('orders.orders'))
    else:
        return redirect(url_for('define_decision.decision'))
    

@auth_bp.route('/createAccount', methods=['GET', 'POST'])
def createAccount():
    if request.method == "GET":
        return render_template('createAccount.html')

    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    if not nome or not email or not senha:
        flash("Informe todos os campos", "erro")
        return redirect(url_for('auth.createAccount'))


    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuarios WHERE Usuario_email = %s", (email,))
    if cursor.fetchone():
        flash("ESTE EMAIL JÁ ESTÁ CADASTRADO NO SISTEMA", "erro")
        cursor.close()
        conn.close()
        return redirect(url_for('auth.createAccount'))

    sql = "INSERT INTO Usuarios (Usuario_nome, Usuario_email, Usuario_senha, Usuario_tipo) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, email, senha, 0))
    conn.commit()

    cursor.close()
    conn.close()

    session['logado'] = True
    return redirect(url_for('orders.orders'))
