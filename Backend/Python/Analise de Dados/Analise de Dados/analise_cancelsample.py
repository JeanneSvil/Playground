import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("Backend/Python/Analise de Dados/Analise de Dados/cancelamentos_sample.csv")
#print(tabela)

tabela = tabela.drop(columns= "CustomerID")
#print(tabela)

#print(tabela.info())

tabela.dropna()
#print(tabela.info())

#print(tabela["cancelou"].value_counts())

#print(tabela["cancelou"].value_counts(normalize=True))

#grafico = px.histogram(tabela, x= 'idade', color= 'cancelou')
grafico = sns.histplot(data= tabela, x="idade", hue="cancelou", multiple="stack", palette=["red", "blue"])
plt.show()

grafico = sns.histplot(data= tabela, x= 'duracao_contrato', hue='cancelou', multiple= 'stack', palette=["red", "blue"])
plt.show()

"""
for coluna in tabela.columns:
    grafico = sns.histplot(data= tabela, x= coluna, hue='cancelou', multiple= 'stack', palette=["red", "blue"])
    plt.show()
"""

tabela = tabela[tabela["ligacoes_callcenter"]<=4]
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
print(tabela["cancelou"].value_counts(normalize=True))
