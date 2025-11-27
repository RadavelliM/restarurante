from flask import Blueprint, render_template, redirect, url_for, flash, session

orders_bp = Blueprint("orders", __name__, url_prefix='')


@orders_bp.route('/orders')
def orders():

    if not session.get('logado'):
        flash('Você precisa estar logado para acessar o site!', 'erro')
        return redirect(url_for('auth.login'))

    return render_template('orders.html')
