from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..db_connexion import get_db_connection

stock_bp = Blueprint("stock", __name__)


@stock_bp.route('/Stock/list')
def list_stock():
    if not session.get('logado'):
        flash('Você precisa estar logado para acessar o site!', 'erro')
        return redirect(url_for('auth.login'))
    if session.get('tipo') == 0:
        return redirect(url_for('error_permission.controlDenied'))

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM Ingredientes'
    cursor.execute(sql)
    datafetch = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('listStock.html', stock=datafetch)


@stock_bp.route('/Stock/create', methods=['GET', 'POST'])
def create_stock():
    if not session.get('logado'):
        flash('Você precisa estar logado para acessar o site!', 'erro')
        return redirect(url_for('auth.login'))
    if session.get('tipo') == 0:
        return redirect(url_for('error_permission.controlDenied'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        qtd = request.form.get('quantidade')
        medida = request.form.get('medida')

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''INSERT INTO Ingredientes 
                 (Ingrediente_nome, Ingrediente_qtd, Ingrediente_un_medida) 
                 VALUES (%s, %s, %s)'''
        cursor.execute(sql, (nome, qtd, medida))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Atualizado com sucesso!', 'sucesso')
        return redirect(url_for('stock.list_stock'))

    return render_template('createStock.html')


@stock_bp.route('/Stock/edit/<int:id>', methods=['GET', 'POST'])
def update_stock(id):
    if not session.get('logado'):
        flash('Você precisa estar logado para acessar o site!', 'erro')
        return redirect(url_for('auth.login'))
    if session.get('tipo') == 0:
        return redirect(url_for('error_permission.controlDenied'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        qtd = request.form.get('quantidade')
        medida = request.form.get('medida')

        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''UPDATE Ingredientes 
                 SET Ingrediente_nome = %s, Ingrediente_qtd = %s, Ingrediente_un_medida = %s 
                 WHERE Ingrediente_id = %s'''
        cursor.execute(sql, (nome, qtd, medida, id))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Atualizado com sucesso!', 'sucesso')
        return redirect(url_for('stock.list_stock'))

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM Ingredientes WHERE Ingrediente_id = %s'
    cursor.execute(sql, (id,))
    item = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template('updateStock.html', item=item)


@stock_bp.route('/Stock/delete/<int:id>')
def delete_stock(id):
    if not session.get('logado'):
        flash('Você precisa estar logado para acessar o site!', 'erro')
        return redirect(url_for('auth.login'))
    if session.get('tipo') == 0:
        return redirect(url_for('error_permission.controlDenied'))

    conn = get_db_connection()
    cursor = conn.cursor()
    sql = 'DELETE FROM Ingredientes WHERE Ingrediente_id = %s'
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Atualizado com sucesso!', 'sucesso')
    return redirect(url_for('stock.list_stock'))
