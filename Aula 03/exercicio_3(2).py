import requests
import json
import pandas as pd

# Acessando a API:
requisicaoDolar = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
requisicaoEuro = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')

# Desserialização do retorno da API:
cotacaoDolar = requisicaoDolar.json()
cotacaoDolar = cotacaoDolar['USD']['bid'] # bid => compra | ask => Venda | varBid => Variação | pctChange => Porcentagem de Variação | high => Máximo | low => Mínimo
cotacaoDolar = float(cotacaoDolar)
cotacaoDolar = "%.2f" % cotacaoDolar

cotacaoEuro = requisicaoEuro.json()
cotacaoEuro = cotacaoEuro['EUR']['bid']
cotacaoEuro = float(cotacaoEuro)
cotacaoEuro = "%.2f" % cotacaoEuro

# Conhecendo a estrutura de dados:
# print('Moeda: '+cotacaoDolar['USD']['name'])
# print (‘Data: ‘ + cotacao[‘USD’][‘create_date’])
# print(‘Valor atual: R$’ + cotacao[‘USD’][‘bid’]))

tabela = pd.read_excel(r'G:\DEV_Codigos\vscode\Curso Intensivão Python\Aula 03\material\Produtos.xlsx')

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = cotacaoDolar
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = cotacaoEuro

# "%.2f"
precoCompra = tabela["Preço de Compra"]
precoCompra = float(precoCompra)

# tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
# tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)