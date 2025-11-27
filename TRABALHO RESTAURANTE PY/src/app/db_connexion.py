import pymssql

# MODELO DE CONEXAO PARA AUTENTICACAO DO WINDOWS
# CASO FOR USAR SQL LOGIN, USAR O MODELO ABAIXO ↓↓↓

# try:
#     def get_db_connection():
#         return pymssql.connect(
#         server=r'localhost\SQLSERVERTESTE',
#         user='sa',
#         password='ADMIN123',
#         database='RESTAURANTESEA',
#         as_dict=True
#     )
# except ValueError as er:
#     print("erro na conexao do banco de dados: ", er)



try:
    def get_db_connection():
        return pymssql.connect(
            server=r'localhost',
            database='RESTAURANTESEA',
            as_dict=True
        )
except ValueError as er:
    print("erro na conexao do banco de dados: ", er)