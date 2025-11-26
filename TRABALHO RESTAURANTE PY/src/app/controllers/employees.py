from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..db_connexion import get_db_connection
import datetime

employees_bp = Blueprint(
    "employees",
    __name__,
    url_prefix="/employees"
)


class CRUDemployees:

    @employees_bp.route('/list')
    def list_employees():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))
        if session.get('tipo') < 2:
            return redirect(url_for('error_permission.controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = '''
            SELECT * FROM Funcionarios
            JOIN Cargos ON Funcionarios.Cargo_id = Cargos.Cargo_id
        '''
        cursor.execute(sql)
        datafetch = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('listEmployees.html', employees=datafetch)

    @employees_bp.route('/create', methods=['GET', 'POST'])
    def create_employees():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))
        if session.get('tipo') < 2:
            return redirect(url_for('error_permission.controlDenied'))

        if request.method == 'POST':
            nome = request.form.get('nome')
            CPF = request.form.get('CPF')
            nascimento = request.form.get('nascimento')
            email = request.form.get('email')
            telefone = request.form.get('telefone')
            salario = request.form.get('salario')
            cargo = request.form.get('cargo')

            conn = get_db_connection()
            cursor = conn.cursor()
            sql = '''
                INSERT INTO Funcionarios 
                (Funcionario_nome, Funcionario_CPF, Funcionario_dt_nasc, Funcionario_email, 
                 Funcionario_telefone, Funcionario_salario, Cargo_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(sql, (nome, CPF, nascimento, email, telefone, salario, cargo))
            conn.commit()
            cursor.close()
            conn.close()

            flash('Cadastrado com sucesso!', 'sucesso')
            return redirect(url_for('employees.list_employees'))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cargos")
        cargos = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('createEmployees.html', cargos=cargos)

    @employees_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
    def update_employees(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))
        if session.get('tipo') < 2:
            return redirect(url_for('error_permission.controlDenied'))

        if request.method == 'POST':
            nome = request.form.get('nome')
            CPF = request.form.get('CPF')
            nascimento = request.form.get('nascimento')
            email = request.form.get('email')
            telefone = request.form.get('telefone')
            salario = request.form.get('salario')
            cargo = request.form.get('cargo')

            conn = get_db_connection()
            cursor = conn.cursor()
            sql = '''
                UPDATE Funcionarios 
                SET Funcionario_nome=%s, Funcionario_CPF=%s, Funcionario_dt_nasc=%s,
                    Funcionario_email=%s, Funcionario_telefone=%s, Funcionario_salario=%s,
                    Cargo_id=%s
                WHERE Funcionario_id=%s
            '''
            cursor.execute(sql, (nome, CPF, nascimento, email, telefone, salario, cargo, id))
            conn.commit()
            cursor.close()
            conn.close()

            flash('Atualizado com sucesso!', 'sucesso')
            return redirect(url_for('employees.list_employees'))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Funcionarios WHERE Funcionario_id = %s", (id,))
        employee = cursor.fetchone()
        cursor.close()
        conn.close()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cargos")
        cargos = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('updateEmployees.html', employees=employee, cargos=cargos)

    @employees_bp.route('/delete/<int:id>')
    def delete_employees(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))
        if session.get('tipo') < 2:
            return redirect(url_for('error_permission.controlDenied'))

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Funcionarios WHERE Funcionario_id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Removido com sucesso!', 'sucesso')
        return redirect(url_for('employees.list_employees'))

    @employees_bp.route('/user/<int:id>', methods=['GET', 'POST'])
    def create_user_employee(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('auth.login'))
        if session.get('tipo') < 2:
            return redirect(url_for('error_permission.controlDenied'))

        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')

            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Usuarios (Usuario_nome, Usuario_email, Usuario_senha, Usuario_tipo) VALUES (%s, %s, %s, %s)",
                (nome, email, senha, 1)
            )
            conn.commit()
            cursor.close()
            conn.close()

            flash('Usuário criado com sucesso!', 'sucesso')
            return redirect(url_for('clients.list_clients'))


        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Funcionarios WHERE Funcionario_id = %s", (id,))
        employee = cursor.fetchone()
        cursor.close()
        conn.close()

        return render_template('createEmployeeAccess.html', employees=employee)


