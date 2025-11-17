from flask import Flask, render_template, request, flash, url_for, session, redirect
import pyodbc # biblioteca de conexao sgbd sql server

# para conectar python com sql server, é necessario um driver odbc. LINK ABAIXO ⭣
"https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17"

app = Flask(__name__)
app.secret_key = 'segredo_super_importante'  # necessário para usar session


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

class Router:
    def __init__(self):
        pass

    @app.route('/')
    def main():
        session['logado'] = False
        return render_template('index.html')

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
                    if session.get('logado'):
                        return redirect(url_for('orders'))
                else:
                    flash('Email ou senha incorretos', 'erro')
                    return redirect(url_for('login'))
            else:
                flash('Informe todos os campos', 'erro') 
                return redirect(url_for('login'))

        return render_template('login.html')

    @app.route('/createAccount', methods=['GET', 'POST'])
    def createAccount():
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
            
            if nome and email and senha:
                sql = 'INSERT Usuarios (Usuario_nome, Usuario_email, Usuario_senha, Usuario_tipo) VALUES (?, ?, ?, ?)'
                cursor.execute(sql, nome, email, senha, 0) 
                cursor.commit()
                session['logado'] = True
                if session.get('logado'):
                    return redirect(url_for('orders'))
            else:
                flash('Informe todos os campos', 'erro') 
                return redirect(url_for('createAccount'))
            
        return render_template('createAccount.html')

    @app.route('/orders')
    def orders():
        return render_template('orders.html')
        
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

routers = Router()
routers.main
routers.login
routers.createAccount
routers.page_not_found

if __name__ == '__main__':
    app.run(debug=True)
