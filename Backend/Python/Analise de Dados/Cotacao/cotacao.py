import requests
import pandas as pd
from datetime import datetime
import time

for i in range(10):
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    tabela = pd.read_excel("Backend/Python/Analise de Dados/Cotacao/Cotações.xlsx")
    tabela.loc[0, "Cotação"] = float(cotacao_dolar)
    tabela.loc[1, "Cotação"] = float(cotacao_euro)
    tabela.loc[2, "Cotação"] = float(cotacao_btc) * 1000
    tabela.loc[0, "Data da Última Atualização"] = datetime.now()

    tabela.to_excel("Cotações.xlsx", index=False)
    print(f"Cotação Atualizada. {datetime.now()}")

    time.sleep(30)