from mysql.connector import connect
import desafioPYTHON as df
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

#Conexão com o MySQL
def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host = host,
        user = user,
        passwd = passwd,
        database = database
    )
    return connection

connection = mysql_connection('localhost', 'root', '')

#Abrindo o arquivo para criação do banco de dados
with open('bancodedados.sql', 'r') as file:
    sql_script = file.read()

cursor = connection.cursor()

cursor.execute(sql_script)

connection = mysql_connection('localhost', 'root', '', 'desafiosql')

cursor = connection.cursor()

#Inserindo os dados do arquivo csv no BD
for cliente in df.copia['Cliente'].unique():
    query = "INSERT INTO cliente (ClienteN) VALUES (%s)"
    values = (str(cliente),)
    cursor.execute(query, values)

for timevenda in df.copia['Equipe'].unique():
    query = "INSERT INTO timevenda (TimeN) VALUES (%s)"
    timeN = str(timevenda).removeprefix("Time ")
    values = (timeN,)
    cursor.execute(query, values)

for vendedor in df.copia['Vendedor'].unique():
    query = "INSERT INTO vendedor (VendedorN) VALUES (%s)"
    VendedorN = str(vendedor).removeprefix("Vendedor ")
    values = (VendedorN,)
    cursor.execute(query, values)

df_unique = df.copia.drop_duplicates(subset=['Equipe', 'Vendedor'])

for index, row in df_unique.iterrows():
    query = "INSERT INTO equipe (TimeN, VendedorN) VALUES (%s,%s)"
    equipeN = str(row['Equipe']).removeprefix("Time ")
    VendedorN = str(row['Vendedor']).removeprefix("Vendedor ")
    values = (equipeN, VendedorN,)
    cursor.execute(query, values)

df.copia['Data da Venda'] = pd.to_datetime(df.copia['Data da Venda'], format='%d/%m/%Y')

df.copia['Data da Venda'] = df.copia['Data da Venda'].dt.date

df_unique = df.copia.drop_duplicates(subset=['ID', 'Cliente', 'Vendedor'])

for index, row in df.copia.iterrows():
    query = "INSERT INTO venda (ClienteN, VendedorN, ID, VendaTipo, DataDeVenda, Categoria, DuracaoDoContrato, Regional, Valor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    ClienteN = str(row['Cliente'])
    VendedorN = str(row['Vendedor']).removeprefix("Vendedor ")
    ID = str(row['ID']).replace("-", "")
    VendaTipo = str(row['Tipo'])
    Data = str(row['Data da Venda'])
    Categoria = str( row['Categoria'])
    Duracao = str(row['Duração do Contrato (Meses)'])
    Regional = str(row['Regional'])
    Valor = str(row['Valor'])
    values = (ClienteN, VendedorN,ID,VendaTipo,Data,Categoria,Duracao,Regional,Valor,)
    cursor.execute(query, values)

connection.commit()
print(cursor.rowcount, "record inserted.")
#Abrindo o arquivo com os exercícios de SQL
with open('exerciciosSQL.sql', 'r') as file:
    sql_script = file.read()

cursor = connection.cursor()

cursor.execute(sql_script)

#Plotando o gráfico de vendas trimestral
query = "SELECT * FROM vendas_trimestral;"

df = pd.read_sql_query(query, connection)

plt.figure(figsize=(10, 6))
for ano in df['ano'].unique():
    df_ano = df[df['ano'] == ano]
    plt.plot(df_ano['trimestre'], df_ano['total_vendas'], marker='o', label=str(ano))

plt.xlabel('Trimestre')
plt.ylabel('Total de Vendas')
plt.title('Histórico de Vendas Trimestral')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

connection.close()
