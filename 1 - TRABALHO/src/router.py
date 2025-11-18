# para conectar python com sql server, é necessario um driver odbc. LINK ABAIXO ⭣
"https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17"

from flask import Flask, render_template, request, flash, url_for, session, redirect
import pyodbc # biblioteca de conexao sgbd sql server
app = Flask(__name__)
app.secret_key = 'segredo_super_importante'  # necessário para usar session

# CONEXAO COM O BANCO DE DADOS
server = r'localhost\SQLSERVERTESTE'
database = 'RESTAURANTESEA'
username = 'sa'
password = 'ADMIN123'

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};" # driver necessario para conexao python - sql server
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "TrustServerCertificate=yes;"
    "Encrypt=no;"
)

conn = pyodbc.connect(conn_str, timeout=5)
cursor = conn.cursor()


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
            return redirect(url_for('login'))
        return render_template('orders.html')
    
obj_client_order = Orders()
obj_client_order.orders


# rota para caso o usuario tente acessar uma area que ele nao tem acesso = controle negado = control denied
# https://www.google.com/search?q=control+denied&rlz=1C1GCEA_enBR987BR987&oq=control&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyDQgCEAAYgwEYsQMYgAQyDQgDEAAYgwEYsQMYgAQyCggEEAAYsQMYgAQyDQgFEAAYgwEYsQMYgAQyDQgGEAAYgwEYsQMYgAQyBggHEEUYPNIBCDE4NDBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8

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

    @app.route('/decision')
    def decision():
        if not session.get('logado'):
            return redirect(url_for('login'))
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        return render_template('decision.html')
    
obj_decision = Decision()
obj_decision.decision



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
                sql = 'INSERT INTO Usuarios (Usuario_nome, Usuario_email, Usuario_senha, Usuario_tipo) VALUES (?, ?, ?, ?)'
                cursor.execute(sql, nome, email, senha, 0)
                cursor.commit()

                query = 'SELECT * FROM Usuarios WHERE Usuario_email = ?'
                cursor.execute(query, email)
                user = cursor.fetchone()

                session['logado'] = True
                session['tipo'] = user.Usuario_tipo
                return redirect(url_for('orders'))
            else:
                flash('Informe todos os campos', 'erro')
                return redirect(url_for('createAccount'))
            
        def verify_email():
            if request.method == 'POST':
                nome = request.form.get('nome')
                email = request.form.get('email')
                senha = request.form.get('senha')
                    
                if email:
                    sql = "SELECT * FROM Usuarios WHERE Usuario_email = ?"
                    cursor.execute(sql, email)
                    user = cursor.fetchone()

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
                sql = "SELECT * FROM Usuarios WHERE Usuario_email = ? AND Usuario_senha = ?"
                cursor.execute(sql, email, senha)
                user = cursor.fetchone()
                if user:
                    session['logado'] = True
                    session['tipo'] = user.Usuario_tipo
                    if session.get('logado'):
                        if user.Usuario_tipo == 0:
                            return redirect(url_for('orders'))
                        if user.Usuario_tipo == 1:
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




class UpdateStock():
    def __init__(self):
        pass
    @app.route('/UpdateStock')
    def update_stock():

        if not session.get('logado'):
            return redirect(url_for('login'))
        
        if session.get('tipo') == 0:
            return redirect(url_for('controlDenied'))
        
        # CONTINUAR AQUI  = FAZER LISTAGEM DOS PRODUTOS
        
        return render_template('updateStock.html')    
        

if __name__ == '__main__':
    app.run(debug=True)