from flask import Flask
from .db_connexion import get_db_connection
import os

def create_app():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    app = Flask(
        __name__,
        template_folder=os.path.join(base_dir, 'Templates'),
        static_folder=os.path.join(base_dir, 'static')
    )
    app.secret_key = "segredo_super_importante" 

    # Rotas modularizadas (Blueprints)
    from .controllers.main import main_bp
    from .controllers.auth import auth_bp
    from .controllers.employees import employees_bp
    from .controllers.clients import clients_bp
    from .controllers.orders import orders_bp
    from .controllers.stock import stock_bp
    from .controllers.error_permission import error_permission_bp
    from .controllers.decision import define_decision_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(employees_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(stock_bp)
    app.register_blueprint(error_permission_bp)
    app.register_blueprint(define_decision_bp)

    return app