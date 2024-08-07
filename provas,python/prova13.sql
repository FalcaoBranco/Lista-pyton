CREATE DATABASE MeuBancoDeDados;

USE MeuBancoDeDados;

CREATE TABLE Clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(255),
    email VARCHAR(255),
    telefone VARCHAR(20)
);

CREATE TABLE Vendas (
    id INT PRIMARY KEY,
    id_cliente INT,
    data DATE,
    valor DECIMAL(10, 2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);
