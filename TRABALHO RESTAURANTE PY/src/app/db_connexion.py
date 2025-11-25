import pymssql

def get_db_connection():
    return pymssql.connect(
        server=r'localhost\SQLSERVERTESTE',
        user='sa',
        password='ADMIN123',
        database='RESTAURANTESEA',
        as_dict=True
    )
