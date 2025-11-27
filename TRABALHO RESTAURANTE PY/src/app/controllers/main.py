from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..db_connexion import get_db_connection

main_bp = Blueprint("main", __name__)

class MainRouterIndex():
    def __init__(self):
        pass
    @main_bp.route('/')
    def main():
        session['logado'] = False
        return render_template('index.html')

obj_render_index = MainRouterIndex()
obj_render_index.main