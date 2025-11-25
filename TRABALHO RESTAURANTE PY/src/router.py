from flask import Flask, render_template, request, flash, url_for, session, redirect
import pymssql

app = Flask(__name__)
app.secret_key = 'segredo_super_importante'

# Configurações do banco (para pymssql)
server = 'localhost\\SQLSERVERTESTE'  # Note: pymssql usa backslash normal, não raw string
database = 'RESTAURANTESEA'
username = 'sa'
password = 'ADMIN123'

# Classe auxiliar para conexão (opcional, mas evita repetição)
def get_db_connection():
    return pymssql.connect(
        server=server,
        user=username,
        password=password,
        database=database,
        as_dict=True  # Mantém como tupla para compatibilidade com índices
    )

class MainRouterIndex():
    def __init__(self):
        pass
    @app.route('/')
    def main():
        session['logado'] = False
        return render_template('index.html')

obj_render_index = MainRouterIndex()
obj_render_index.main

class Error():
    def __init__(self):
        pass
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

obj_error_404 = Error()
obj_error_404.page_not_found

class Orders():
    def __init__(self):
        pass
    @app.route('/orders')
    def orders():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        return render_template('orders.html')

obj_client_order = Orders()
obj_client_order.orders

class OutPermission():
    def __init__(self):
        pass
    @app.route('/controlDenied')
    def controlDenied():
        return render_template('outPermission.html')

obj_control_denied = OutPermission()
obj_control_denied.controlDenied

class Decision():
    def __init__(self):
        pass
    @app.route('/decision/employee')
    def decision():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        if session.get('tipo') == 2:
            return redirect(url_for('decision_manager'))
        return render_template('decision.html')

obj_decision = Decision()
obj_decision.decision

class DecisionManager:
    def __init__(self):
        pass
    @app.route('/decision/manager')
    def decision_manager():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') < 2:
            return redirect(url_for('controlDenied'))
        return render_template('decision2.html')

class CreateAccount():
    def __init__(self):
        pass

    @app.route('/createAccount')
    def render_create_account():
        return render_template('createAccount.html')
    
    @app.route('/createAccount', methods=['GET', 'POST'])
    def createAccount():
        def insert_user(nome, email, senha):
            if nome and email and senha:
                conn = get_db_connection()
                cursor = conn.cursor()
                sql = 'INSERT INTO Usuarios (Usuario_nome, Usuario_email, Usuario_senha, Usuario_tipo) VALUES (%s, %s, %s, %s)'
                cursor.execute(sql, (nome, email, senha, 0))
                conn.commit()

                query = 'SELECT * FROM Usuarios WHERE Usuario_email = %s'
                cursor.execute(query, (email,))
                user = cursor.fetchone()

                cursor.close()
                conn.close()

                if user:
                    session['logado'] = True
                    session['tipo'] = user['Usuario_tipo']  # coluna Usuario_tipo (5ª coluna → índice 4)
                    return redirect(url_for('orders'))
                else:
                    flash('Erro ao criar usuário.', 'erro')
                    return redirect(url_for('createAccount'))
            else:
                flash('Informe todos os campos', 'erro')
                return redirect(url_for('createAccount'))
            
        def verify_email():
            if request.method == 'POST':
                nome = request.form.get('nome')
                email = request.form.get('email')
                senha = request.form.get('senha')

                if email:
                    conn = get_db_connection()
                    cursor = conn.cursor()
                    sql = "SELECT * FROM Usuarios WHERE Usuario_email = %s"
                    cursor.execute(sql, (email,))
                    user = cursor.fetchone()
                    cursor.close()
                    conn.close()

                    if user:
                        flash('ESTE EMAIL JÁ ESTÁ CADASTRADO NO SISTEMA', 'erro')
                        return redirect(url_for('createAccount'))
                    
                    return insert_user(nome, email, senha)
            return render_template('createAccount.html')
        return verify_email()

obj_create_account = CreateAccount()
obj_create_account.render_create_account
obj_create_account.createAccount

class Login:
    def __init__(self):
        pass

    @app.route('/login')
    def render_login():
        return render_template('login.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            senha = request.form.get('senha')

            if email and senha:
                conn = get_db_connection()
                cursor = conn.cursor()
                sql = "SELECT * FROM Usuarios WHERE Usuario_email = %s AND Usuario_senha = %s"
                cursor.execute(sql, (email, senha))
                user = cursor.fetchone()
                cursor.close()
                conn.close()

                if user:
                    session['logado'] = True
                    session['tipo'] = user['Usuario_tipo']  # Usuario_tipo

                    if user['Usuario_tipo'] == 0:
                        return redirect(url_for('orders'))
                    else:
                        return redirect(url_for('decision'))
                else:
                    flash('Email ou senha incorretos', 'erro')
                    return redirect(url_for('login'))
            else:
                flash('Informe todos os campos', 'erro')
                return redirect(url_for('login'))

obj_user_login = Login()
obj_user_login.render_login
obj_user_login.login

class CRUDstock():
    def __init__(self):
        pass

    @app.route('/Stock/list')
    def list_stock():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM Ingredientes'
        cursor.execute(sql)
        datafetch = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('listStock.html', stock=datafetch)
    
    @app.route('/Stock/create', methods=['GET', 'POST'])
    def create_stock():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        if request.method == 'POST':
            nome = request.form.get('nome')
            qtd = request.form.get('quantidade')
            medida = request.form.get('medida')

            conn = get_db_connection()
            cursor = conn.cursor()
            sql = 'INSERT INTO Ingredientes (Ingrediente_nome, Ingrediente_qtd, Ingrediente_un_medida) VALUES (%s, %s, %s)'
            cursor.execute(sql, (nome, qtd, medida))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Atualizado com sucesso!', 'sucesso')
            return redirect(url_for('list_stock'))
        
        return render_template('createStock.html')
    
    @app.route('/Stock/edit/<int:id>', methods=['GET', 'POST'])
    def update_stock(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        if request.method == 'POST':
            nome = request.form.get('nome')
            qtd = request.form.get('quantidade')
            medida = request.form.get('medida')

            conn = get_db_connection()
            cursor = conn.cursor()
            sql = 'UPDATE Ingredientes SET Ingrediente_nome = %s, Ingrediente_qtd = %s, Ingrediente_un_medida = %s WHERE Ingrediente_id = %s'
            cursor.execute(sql, (nome, qtd, medida, id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Atualizado com sucesso!', 'sucesso')
            return redirect(url_for('list_stock'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM Ingredientes WHERE Ingrediente_id = %s'
        cursor.execute(sql, (id,))
        item = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('updateStock.html', item=item)
    
    @app.route('/Stock/delete/<int:id>')
    def delete_stock(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DELETE FROM Ingredientes WHERE Ingrediente_id = %s'
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Atualizado com sucesso!', 'sucesso')
        return redirect(url_for('list_stock'))

obj_update_stock = CRUDstock()
obj_update_stock.list_stock
obj_update_stock.create_stock
obj_update_stock.update_stock

class CRUDclients():
    def __init__(self):
        pass

    @app.route('/Clients/list')
    def list_clients():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM Usuarios WHERE Usuario_tipo = 0'
        cursor.execute(sql)
        datafetch = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('listClients.html', clients=datafetch)
    
    @app.route('/Clients/delete/<int:id>')
    def delete_clients(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DELETE FROM Usuarios WHERE Usuario_id = %s'
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Atualizado com sucesso!', 'sucesso')
        return redirect(url_for('list_clients'))

class CRUDemployees():
    def __init__(self):
        pass

    @app.route('/Employees/list')
    def list_employees():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') < 2:
            return redirect(url_for('controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'SELECT * FROM Funcionarios, Cargos WHERE Funcionarios.Cargo_id = Cargos.Cargo_id'
        cursor.execute(sql)
        datafetch = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('listEmployees.html', employees=datafetch)
    
    @app.route('/Employees/create', methods=['GET', 'POST'])
    def create_employees():
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') < 2:
            return redirect(url_for('controlDenied'))
        
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
            sql = 'INSERT INTO Funcionarios (Funcionario_nome, Funcionario_CPF, Funcionario_dt_nasc, Funcionario_email, Funcionario_telefone, Funcionario_salario, Cargo_id) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (nome, CPF, nascimento, email, telefone, salario, cargo))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Atualizado com sucesso!', 'sucesso')
            return redirect(url_for('list_employees'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM Cargos'
        cursor.execute(query)
        datafetch = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('createEmployees.html', cargos=datafetch)
    
    @app.route('/Employees/edit/<int:id>', methods=['GET', 'POST'])
    def update_employees(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') < 2:
            return redirect(url_for('controlDenied'))
        
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
            sql = 'UPDATE Funcionarios SET Funcionario_nome = %s, Funcionario_CPF = %s, Funcionario_dt_nasc = %s, Funcionario_email = %s, Funcionario_telefone = %s, Funcionario_salario = %s, Cargo_id = %s WHERE Funcionario_id = %s'
            cursor.execute(sql, (nome, CPF, nascimento, email, telefone, salario, cargo, id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Atualizado com sucesso!', 'sucesso')
            return redirect(url_for('list_employees'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sqlEMP = 'SELECT * FROM Funcionarios WHERE Funcionario_id = %s'
        cursor.execute(sqlEMP, (id,))
        employees = cursor.fetchone()
        cursor.close()
        conn.close()

        conn = get_db_connection()
        cursor = conn.cursor()
        sqlCARG = 'SELECT * FROM Cargos'
        cursor.execute(sqlCARG)
        cargos = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template('updateEmployees.html', employees=employees, cargos=cargos)
    
    @app.route('/Employees/delete/<int:id>')
    def delete_employees(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') < 2:
            return redirect(url_for('controlDenied'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = 'DELETE FROM Funcionarios WHERE Funcionario_id = %s'
        cursor.execute(sql, (id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Atualizado com sucesso!', 'sucesso')
        return redirect(url_for('list_employees'))

    @app.route('/Employees/user/<int:id>', methods=['GET', 'POST'])
    def create_user_employee(id):
        if not session.get('logado'):
            flash('Você precisa estar logado para acessar o site!', 'erro')
            return redirect(url_for('login'))
        if session.get('tipo') < 2:
            return redirect(url_for('controlDenied'))
        
        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            senha = request.form.get('senha')

            conn = get_db_connection()
            cursor = conn.cursor()
            sql = 'INSERT INTO Usuarios (Usuario_nome, Usuario_email, Usuario_senha, Usuario_tipo) VALUES (%s, %s, %s, %s)'
            cursor.execute(sql, (nome, email, senha, 1))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Atualizado com sucesso!', 'sucesso')
            return redirect(url_for('list_clients'))
        
        conn = get_db_connection()
        cursor = conn.cursor()
        sqlEMP = 'SELECT * FROM Funcionarios WHERE Funcionario_id = %s'
        cursor.execute(sqlEMP, (id,))
        employees = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('createEmployeeAccess.html', employees=employees)

obj_employees = CRUDemployees()
obj_employees.list_employees
obj_employees.create_employees
obj_employees.update_employees
obj_employees.delete_employees
obj_employees.create_user_employee

if __name__ == '__main__':
    app.run(debug=True)