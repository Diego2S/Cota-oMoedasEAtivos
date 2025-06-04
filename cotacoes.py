import requests
import os
import yfinance as yf
from time import sleep 

# API com limite de 100 mil requesiçoes por mês

def pegar_cotacao( moeda, paramoeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-{paramoeda}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao = dados[f'{moeda}{paramoeda}']['bid']
        cotacao = float(cotacao)
        print(f"Cotação atual do {moeda} para {paramoeda}: "+f"{cotacao:,.3f}"
              .replace(",", "X").replace(".", ",").replace("X", "."))
    else:
        print(f"Erro ao buscar cotação. {moeda}-{paramoeda}")




def pegar_cotacao_acao(ticker):
    acao = yf.Ticker(ticker)
    dados = acao.history(period="1d")

    if not dados.empty:
        preco_atual = dados['Close'].iloc[-1]
        print(f"{ticker} está valendo R$ {preco_atual:.2f}")
    else:
        print(f"Não foi possível obter dados para {ticker}.")

# Exemplos: PETR4.SA, VALE3.SA, ITUB4.SA




conta = 0
while True:
    
    if conta == 5:
        print('Finalizado')
        break

    pegar_cotacao('USD','BRL')
    pegar_cotacao('BTC','BRL')
    pegar_cotacao('ETH','BRL')
    pegar_cotacao('JPY','BRL')
    pegar_cotacao_acao("RANI3.SA")
    pegar_cotacao_acao("TAEE4.SA")
    print(conta)
    sleep(2)
    conta +=1
    
    os.system('clear')
    