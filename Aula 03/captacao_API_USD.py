import requests
import json
# Acessando a API:
requisicaoDolar = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
requisicaoEuro = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
requisicaoOuro = requests.get('https://www.metals-api.com/api/latest?access_key=dosk9uce9r4yyc4cqzmj1cf0pszt4oikf6ucrwl1w2abu45hb1nfu9dx7alr&base=gold&symbols=XAU%2CXAG%2CXPD%2CXPT%2CXRH')

# Desserialização do retorno da API:
cotacaoDolar = requisicaoDolar.json()
cotacaoEuro = requisicaoEuro.json()
cotacaoOuro = requisicaoOuro.json()

# Conhecendo a estrutura de dados:
# print('Moeda: '+cotacaoDolar['USD']['name'])
# print (‘Data: ‘ + cotacao[‘USD’][‘create_date’])
# print(‘Valor atual: R$’ + cotacao[‘USD’][‘bid’]))

print('Valor atual do Dólar: R$ '+ cotacaoDolar['USD']['bid']) # bid => compra | ask => Venda | varBid => Variação | pctChange => Porcentagem de Variação | high => Máximo | low => Mínimo

print('Valor atual do Euro: R$ '+ cotacaoEuro['EUR']['bid'])
print(cotacaoOuro)
# print('Valor atual do Ouro: R$ '+ cotacaoOuro['GOLD']['xau'])