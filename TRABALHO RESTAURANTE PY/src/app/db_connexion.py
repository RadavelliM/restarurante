import pymssql

# MODELO DE CONEXAO PARA AUTENTICACAO DO WINDOWS
# CASO FOR USAR SQL LOGIN, USAR O MODELO ABAIXO ↓↓↓

# def get_db_connection():
#     return pymssql.connect(
#         server=r'localhost\nome da instancia',
#         user='sa',
#         password='sua senha aqui',
#         database='RESTAURANTESEA',
#         as_dict=True
#     )


def get_db_connection():
    return pymssql.connect(
        server=r'localhost',
        database='RESTAURANTESEA',
        as_dict=True
    )