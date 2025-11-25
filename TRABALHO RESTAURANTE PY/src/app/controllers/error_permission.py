from flask import Blueprint, render_template

# Blueprint sem prefixo, mas pode adicionar se quiser organizar
error_permission_bp = Blueprint("error_permission", __name__)


# ==== PÁGINA 404 PERSONALIZADA ====
@error_permission_bp.app_errorhandler(404)   # <-- mais correto para erros globais
def page_not_found(error):
    return render_template('404.html'), 404


# ==== ERRO DE PERMISSÃO ====
@error_permission_bp.route('/controlDenied')
def controlDenied():
    return render_template('outPermission.html')
