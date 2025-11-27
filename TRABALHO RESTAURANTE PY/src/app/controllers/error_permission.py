from flask import Blueprint, render_template

error_permission_bp = Blueprint("error_permission", __name__)


class ErrorHandling:
    @error_permission_bp.app_errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404


class ControlDenied:
    @error_permission_bp.route('/controlDenied')
    def controlDenied():
        return render_template('outPermission.html')
