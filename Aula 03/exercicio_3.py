# Automação Web - Web Scraping
# selenium => chromedriver

from selenium import webdriver # controlar o navegador
from selenium.webdriver.common.keys import keys #usar o teclado
from selenium.webdriver.common.by import by #localizar os itens no navegador
import pandas as pd
# criar o navegador
navegador = webdriver.Chrome()

# entrar no google e pesquisar por cotação do dolar
navegador.get('http://www.google.com')

# pegar a cotação do dolar
# navegador.find_element(qual o parametro que você quer usar, e qual o código)
navegador.find_element(By. XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element(By. XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').sende_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').get_atribute('data-value')

# entrar no google e pesquisar por cotação do euro
navegador.get('http://www.google.com')

# pegar a cotação do euro
# navegador.find_element(qual o parametro que você quer usar, e qual o código)
navegador.find_element(By. XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').send_keys("cotação euro")
navegador.find_element(By. XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]t').sende_keys(Keys.ENTER)
cotacao_euro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_atribute('data-value')

# entrar no https://www.melhorcambio.com/ouro-hoje
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_atribute('value')
cotacao_ouro = cotacao_ouro.replace(",",".")

navegador.quit()

tabela = pd.read_excel(r'\G:\DEV_Codigos\vscode\Curso Intensivão Python\Aula 03\material\Produtos.xlsx')

# Atualizar as cotações na base de dados

# tabela.loc[linhas, colunas]

#cotacao_dolar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacaoDolar)

#cotacao_euro
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacaoEuro)

print(tabela)

# Atualizar o preço de compra e de venda na base de dados

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela.to_excel("ProdutosAtualizados.xlsx", index=False)