

-- ARQUIVO CONTENDO APENAS OS COMANDOS DE "CREATE" E "ALTER" TABLE
-- EXECUTE ESTE ARQUIVO PRIMEIRO, EM SEQUENCIA, EXECUTE O ARQUIVO "restaurante_inserts.sql" CONTENDO OS COMANDOS DE "INSERT" PARA CARREGAR OS DADOS PREVIOS.

SET DATEFORMAT YMD
IF NOT EXISTS (SELECT * FROM SYS.databases WHERE NAME = 'RESTAURANTESEA')
CREATE DATABASE RESTAURANTESEA
GO

CREATE TABLE Usuarios
(
    Usuario_id INT IDENTITY CONSTRAINT pk_Usuarios PRIMARY KEY,
    Usuario_nome VARCHAR(30),
    Usuario_email VARCHAR(50),
    Usuario_senha VARCHAR(20),
    Usuario_tipo INT -- 0 = cliente, 1 = funcionario, 2 = gerente
)

CREATE TABLE Cargos
(
    Cargo_id INT IDENTITY CONSTRAINT pk_Cargos PRIMARY KEY,
    Cargo_nome VARCHAR(30)
)

CREATE TABLE Funcionarios
(
    Funcionario_id INT IDENTITY CONSTRAINT pk_Funcionarios PRIMARY KEY,
    Funcionario_nome VARCHAR(30),
    Funcionario_CPF VARCHAR(20),
    Funcionario_dt_nasc DATETIME,
    Funcionario_email VARCHAR(50),
    Funcionario_telefone VARCHAR(20),
    Funcionario_salario FLOAT,
    Cargo_id INT
)

CREATE TABLE Ingredientes
(
    Ingrediente_id INT IDENTITY CONSTRAINT pk_Ingrediente PRIMARY KEY,
    Ingrediente_nome VARCHAR(50),
    Ingrediente_qtd FLOAT,
    Ingrediente_un_medida VARCHAR(20),
)


ALTER TABLE Funcionarios ADD CONSTRAINT FK_Funcionario_Cargo FOREIGN
KEY (Cargo_id) REFERENCES Cargos (Cargo_id)
