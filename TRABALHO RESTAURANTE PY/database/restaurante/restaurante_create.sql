

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

CREATE TABLE Pratos
(
    Prato_id INT IDENTITY CONSTRAINT pk_Pratos PRIMARY KEY,
    Prato_nome VARCHAR(50),
    Prato_valor FLOAT,
)

CREATE TABLE Pedidos
(
    Pedido_id INT IDENTITY CONSTRAINT pk_Pedidos PRIMARY KEY,
    Pedido_data DATETIME,
    Pedido_valor_total FLOAT,
    Usuario_id INT,
)

CREATE TABLE Fornecedores
(
    Fornecedor_id INT IDENTITY CONSTRAINT pk_Fornecedores PRIMARY KEY,
    Fornecedor_nome VARCHAR(50),
    Fornecedor_telefone VARCHAR(50),
)

CREATE TABLE Ingredientes_Pratos
(
    Prato_id INT IDENTITY CONSTRAINT pk_Ingrediente_pratos PRIMARY KEY,
    Ingrediente_id INT,
    Ingredientes_Pratos_qtd FLOAT
)

CREATE TABLE Pratos_Pedidos
(
    Pedido_id INT IDENTITY CONSTRAINT pk_pratos_pedidos PRIMARY KEY,
    Prato_id INT,
    Pratos_Pedidos_qtd INT
)

ALTER TABLE Funcionarios ADD CONSTRAINT FK_Funcionario_Cargo FOREIGN
KEY (Cargo_id) REFERENCES Cargos (Cargo_id)

ALTER TABLE Pedidos ADD CONSTRAINT FK_Usuario_Pedido FOREIGN
KEY(Usuario_id) REFERENCES Usuarios (Usuario_id)

ALTER TABLE Ingredientes_Pratos ADD CONSTRAINT FK_Prato_Ingrediente
FOREIGN KEY(Prato_id) REFERENCES Pratos (Prato_id)

ALTER TABLE Ingredientes_Pratos ADD CONSTRAINT FK_Ingrediente_Prato
FOREIGN KEY(Ingrediente_id) REFERENCES Ingredientes (Ingrediente_id)

ALTER TABLE Pratos_Pedidos ADD CONSTRAINT FK_Pedido_Prato FOREIGN
KEY(Pedido_id) REFERENCES Pedidos (Pedido_id)

ALTER TABLE Pratos_Pedidos ADD CONSTRAINT FK_Prato_Pedido FOREIGN
KEY(Prato_id) REFERENCES Pratos (Prato_id)-- Write your own SQL object definition here, and it'll be included in your package.
