CREATE DATABASE MeuBancoDeDados;

USE MeuBancoDeDados;

CREATE TABLE Alunos (
    id SERIAL PRIMARY KEY, 
    nome VARCHAR(255), 
    email VARCHAR(255) 
);

CREATE TABLE Matriculas (
    id SERIAL PRIMARY KEY, 
    id_aluno INT, 
    disciplina VARCHAR(255), 
    nota FLOAT, 
    FOREIGN KEY (id_aluno) REFERENCES Alunos(id) 
)