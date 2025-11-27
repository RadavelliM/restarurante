-- ARQUIVO PARA EXECUTAR CONSULTAS

USE RESTAURANTESEA
GO

SELECT * FROM Usuarios
SELECT * FROM Cargos
SELECT * FROM Funcionarios
SELECT * FROM Ingredientes
SELECT Funcionario_nome, Cargo_nome FROM Funcionarios, Cargos WHERE Funcionarios.Cargo_id = Cargos.Cargo_id
