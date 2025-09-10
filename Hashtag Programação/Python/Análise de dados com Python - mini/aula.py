import pandas as pd
import plotly.express as px

tabela = pd.read_csv(".\ClientesBanco.csv", encoding="latin1")

tabela = tabela.drop("CLIENTNUM", axis=1)

tabela = tabela.dropna() #exclui linhas vazias

print(tabela)

print(tabela.info())

print(tabela.describe().round(1)) #descrição    arrendoandamento e em quantas casas são

#avaliar como esta a divisão entre Clientes x Cancelados
qtde_categoria = tabela["Categoria"].value_counts()
print(qtde_categoria)

#avaliar como esta a divisão entre Clientes x Cancelados, percentual
qtde_categoria_perc = tabela["Categoria"].value_counts(normalize=True)
print(qtde_categoria_perc)

#descobrir o motivo de cancelamento (comparação entre clientes e cancelados)
#grafico = px.histogram(tabela, x="Idade", color="Categoria")
#grafico.show(renderer="browser")

for coluna in tabela:
    grafico = px.histogram(tabela, x=coluna, color="Categoria")
    grafico.show(renderer="browser")