from flask import Blueprint, render_template, redirect, url_for, flash, session
from ..db_connexion import get_db_connection

define_decision_bp = Blueprint(
    "define_decision",
    __name__,
    url_prefix="/decision"
)

class Decision:
    def __init__(self):
        pass

    @define_decision_bp.route('/employee')
    def decision():
        # Verifica login
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))  # <-- CORRIGIDO

        # Permissões
        if session.get('tipo') == 0:
            return redirect(url_for('error_permission.controlDenied'))  # <-- CORRIGIDO

        if session.get('tipo') == 2:
            return redirect(url_for('define_decision.decision_manager'))  # <-- CORRIGIDO

        return render_template('decision.html')


class DecisionManager:
    def __init__(self):
        pass

    @define_decision_bp.route('/manager')
    def decision_manager():
        # Verifica login
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))  # <-- CORRIGIDO

        # Apenas tipo >= 2 pode acessar
        if session.get('tipo') < 2:
            return redirect(url_for('error_permission.controlDenied'))  # <-- CORRIGIDO

        return render_template('decision2.html')
