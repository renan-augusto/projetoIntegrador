CREATE DATABASE REGISTRO_ALUNOS_FAMERP;

USE REGISTRO_ALUNOS_FARMERP;

CREATE TABLE ALUNO (

	IDALUNO INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR (100) NOT NULL,
	CPF CHAR(11) UNIQUE,
	DATANASCIMENTO DATE NOT NULL ,
	SEXO ENUM("M","F") NOT NULL,
	EMAIL VARCHAR(50) UNIQUE,
	SEMESTRE CHAR(1)

);


CREATE TABLE PROFESSOR (

	IDPROFESSOR INT PRIMARY KEY AUTO_INCREMENT,
	NOME VARCHAR (100),
	SEXO ENUM("M", "F"),
	CPF CHAR(11)

);


CREATE TABLE ESTAGIO (

	IDESTAGIO INT PRIMARY KEY AUTO_INCREMENT,
	ID_ALUNO INT,
	FOREIGN KEY (ID_ALUNO)
		REFERENCES ALUNO(IDALUNO),
	ID_PROFESSOR INT,
	FOREIGN KEY (ID_PROFESSOR)
		REFERENCES PROFESSOR(IDPROFESSOR),
	NOME VARCHAR (30) NOT NULL,
	ANO CHAR(4)

);


CREATE TABLE PROGRAMACAO (

	IDPROGRAMACAO INT PRIMARY KEY AUTO_INCREMENT,
	ID_ALUNO INT,
	FOREIGN KEY (ID_ALUNO)
		REFERENCES ALUNO(IDALUNO),
	ID_ESTAGIO INT UNIQUE,
	FOREIGN KEY (ID_ESTAGIO)
		REFERENCES ESTAGIO(IDESTAGIO),
	ID_PROFESSOR INT UNIQUE,
	FOREIGN KEY (ID_PROFESSOR)
		REFERENCES PROFESSOR(IDPROFESSOR),
	DATA DATE,
	HORA TIME


);


CREATE TABLE PRESENCA (

	IDPRESENCA INT PRIMARY KEY AUTO_INCREMENT,
	ID_PROGRAMACAO INT UNIQUE,
	FOREIGN KEY (ID_PROGRAMACAO)
		REFERENCES PROGRAMACAO(IDPROGRAMACAO),
	DATAPRESENCA TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);



