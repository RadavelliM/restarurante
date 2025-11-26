O PROJETO CONTA COM ALGUMAS BIBLIOTECAS E ARQUIVOS QUE PRECISAM SER INSTALADOS E EXECUTADOS ANTES DE RODAR O SISTEMA

1 - INSTALAR O DRIVER ODBC PARA CONECTAR O SQL SERVER COM O BACKEND (PYTHON)
    LINK PARA O DRIVER ODBC → "https://learn.microsoft.com/pt-br/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver17"

2 - EXECUTAR AS BIBLIOTECAS
    • para abrir o terminal para instalar as bibliotecas, use o atalho de teclado CTRL + ' (ASPAS)
    • com o teminal aberto, use o comando pip install com as bibliotecas para instalar

    • pip install flask
    • pip install pyodbc

3 - EXECUTAR ARQUIVOS
    • abra a pasta database/restaurante
    • crie as conexões necessárias para conectar o banco de dados
    • execute o arquivo restaurante_create.sql
    • execute o arquivo restaurante_inserts.sql