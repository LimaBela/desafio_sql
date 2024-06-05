Para utilizar o MySQL, foi usado o XAMPP;
Para exercicios de python, foram usadas as bibliotecas:
	- pandas
	- mysqlconnector
	- datetime
	- matplotlib

##1) Para a primeira parte, foi criado o arquivo desafioPYTHON.py, que executa as seguintes tarefas a partir da leitura do arquivo DB_Teste.csv:

	-Construa uma tabela auxiliar que sumarize o valor vendido por cada vendedor, ordenando do maior para o menor;
	-Imprima e identifica qual foi o cliente responsável pela venda com maior valor e com menor valor;
	-Imprima valor médio por Tipo de venda (Serviços, Licenciamento, Produtos)
	-Imprima o número de vendas realizada por cliente;

##2) Para a segunda parte, foi criado um arquivo principal em python (desafioSQL.py) que executa os arquivos SQL para primeiro criar um banco de dados (bancodedados.sql) para as informações do DB_Teste.csv, e depois para executar as seguintes tarefas:

	- Construa o modelo de relacionamento com as categorias utilizadas em todos os campos do arquivo CSV (colocar imagem);
	- Listar todas as vendas (ID) e seus respectivos clientes apenas no ano de 2020
	- Listar a equipe de cada vendedor

A última tarefa tem a tabela criada neste arquivo e, no arquivo python, é plotado o gráfico:

- Construir uma tabela que avalia trimestralmente o resultado de vendas e plote um gráfico deste histórico.