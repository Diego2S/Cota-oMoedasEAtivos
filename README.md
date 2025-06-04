# Projeto Cotação Automática

Este projeto em Python consulta automaticamente cotações de moedas e ações brasileiras em tempo real, utilizando APIs públicas e a biblioteca `yfinance`.

---

## Funcionalidades

- Consulta cotações de moedas (USD, BTC, ETH, JPY) em relação ao BRL usando a API AwesomeAPI.
- Consulta cotações de ações brasileiras (exemplo: RANI3.SA, TAEE4.SA) usando a biblioteca `yfinance`.
- Atualização das cotações em loop, com limite de 5 iterações e intervalo de 2 segundos entre as consultas.
- Limpeza da tela a cada atualização para facilitar a visualização.

---

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `requests`
  - `yfinance`

Instale as dependências com:

```bash
pip install requests yfinance


## Funcionalidades

    A API https://economia.awesomeapi.com.br possui um limite de 100 mil requisições por mês.

    O script não trata exceções avançadas nem erros de conexão além do status HTTP.

    As cotações de ações são atualizadas com base no último preço de fechamento disponível.


Contato

Desenvolvido por Diego2S.