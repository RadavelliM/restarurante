from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..db_connexion import get_db_connection

clients_bp = Blueprint(
    "clients",             # nome interno do blueprint
    __name__,
    url_prefix="/Clients"  # prefixo de rota
)

class CRUDclients():
    def __init__(self):
        pass

    @clients_bp.route('/list')
    def list_clients():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))  # <-- CORRIGIDO

        if session.get('tipo') == 0:
            return redirect(url_for('error_permission.controlDenied'))  # <-- CORRIGIDO
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM Usuarios WHERE Usuario_tipo = 0'
        cursor.execute(sql)
        datafetch = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('listClients.html', clients=datafetch)
    
    @clients_bp.route('/delete/<int:id>')
    def delete_clients(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))  # <-- CORRIGIDO

        if session.get('tipo') == 0:
            return redirect(url_for('error_permission.controlDenied'))  # <-- CORRIGIDO
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DELETE FROM Usuarios WHERE Usuario_id = %s'
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Atualizado com sucesso!', 'sucesso')

        return redirect(url_for('clients.list_clients'))  # <-- CORRIGIDO
