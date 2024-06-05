/* Criação do banco de dados a partir do modelo relacional */

CREATE DATABASE desafiosql;

USE desafiosql;

CREATE TABLE Cliente (
    ClienteN INT PRIMARY KEY
);

CREATE TABLE TimeVenda (
    TimeN INT PRIMARY KEY
);

CREATE TABLE Vendedor (
    VendedorN INT PRIMARY KEY 
);

CREATE TABLE Equipe (
    TimeN INT,
    VendedorN INT,
    PRIMARY KEY (TimeN,VendedorN),
    FOREIGN KEY (TimeN) REFERENCES TimeVenda (TimeN),
    FOREIGN KEY (VendedorN) REFERENCES Vendedor (VendedorN)
);

CREATE TABLE Venda (
    ClienteN INT,
    VendedorN INT,
    ID INT,
    VendaTipo VARCHAR(50),
    DataDeVenda DATE,
    Categoria VARCHAR(50),
    DuracaoDoContrato INT,
    Regional VARCHAR(50),
    Valor DECIMAL(20,2),
    PRIMARY KEY (ID,DataDeVenda, ClienteN, VendedorN),
    FOREIGN KEY (ClienteN) REFERENCES Cliente (ClienteN),
    FOREIGN KEY (VendedorN) REFERENCES Vendedor (VendedorN)
);
 
