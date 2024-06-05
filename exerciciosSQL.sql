USE desafiosql

SELECT ID, ClienteN
FROM venda
WHERE YEAR(DataDeVenda) = 2020

SELECT *
FROM equipe

CREATE TABLE vendas_trimestral (
    trimestre VARCHAR(20),
    ano INT,
    total_vendas DECIMAL(20, 2)
);

INSERT INTO vendas_trimestral (trimestre, ano, total_vendas)
SELECT 
    CONCAT('Q', QUARTER(DataDeVenda)) AS trimestre,
    YEAR(DataDeVenda) AS ano,
    SUM(DataDeVenda) AS total_vendas
FROM 
    venda
GROUP BY 
    ano, trimestre;