import pandas as pd
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
pd.options.display.float_format = '{:.2f}'.format

arquivo = pd.read_csv('./DB_Teste.csv', sep=";")

copia = arquivo.copy()

#Constantes
CLIENTE = 'Cliente'
ID = 'ID'
VENDEDOR = 'Vendedor'
TIPO = 'Tipo'
LICENCIAMENTO = 'Licenciamento'
SERVICOS = 'Serviços'
PRODUTOS = 'Produtos'
VALOR = 'Valor'

copia[VALOR] = copia[VALOR].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').str.strip().astype(float)

#Valor vendido por cada vendedor
def reais(numero):
    return 'R$ ' + locale.currency(numero, grouping=True, symbol=None)

vendedor = copia.groupby(VENDEDOR)[VALOR].sum().sort_values(ascending=False).reset_index()
vendedor[VALOR] = vendedor[VALOR].apply(reais)

print(vendedor)

#Maior e menor venda
clienteMaior= copia.loc[copia[VALOR].idxmax()][CLIENTE]
valorMaior= copia.loc[copia[VALOR].idxmax()][VALOR]
vMaior = reais (valorMaior)

clienteMenor= copia.loc[copia[VALOR].idxmin()][CLIENTE]
valorMenor= copia.loc[copia[VALOR].idxmin()][VALOR]
vMenor = reais (valorMenor)

print("Cliente com maior valor vendido: ", clienteMaior," Venda:", vMaior)
print("Cliente com menor valor vendido: ", clienteMenor," Venda:", vMenor)


#Valor médio por tipo de venda

ser_licenciamento = copia.loc [copia [TIPO] == LICENCIAMENTO, VALOR]
ser_produtos = copia.loc [copia [TIPO] == PRODUTOS, VALOR]
ser_servicos = copia.loc [copia [TIPO] == SERVICOS, VALOR]

media_lic = ser_licenciamento.mean()
mediaLic = reais(media_lic)
print ("Valor médio em Licenciamento: ", mediaLic)

media_pro = ser_produtos.mean()
mediaPro = reais(media_pro)
print ("Valor médio em Produtos: ", mediaPro)

media_ser = ser_servicos.mean()
mediaSer = reais(media_ser)
print ("Valor médio em Serviços: ", mediaSer)

#Valor de vendas por cliente

copia[CLIENTE] = copia[CLIENTE].str.replace('Cliente', '').str.strip().astype(int)
copia[CLIENTE].sort_values(ascending=True)

vendaCliente = copia.groupby(CLIENTE)[ID].count()

print("Número de vendas realizadas por cliente:\n", vendaCliente)


