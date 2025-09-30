import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("Backend/Python/Analise de Dados/Analise de Dados/cancelamentos.csv")

tabela = tabela.drop(columns= "CustomerID")

tabela = tabela.dropna()
print(tabela.info())

#print(tabela["cancelou"].value_counts())

print(tabela["cancelou"].value_counts(normalize=True))

grafico = sns.histplot(data= tabela, x= 'ligacoes_callcenter', hue='cancelou', multiple= 'stack', palette=["red", "blue"])
plt.show()

grafico = sns.histplot(data= tabela, x= 'dias_atraso', hue='cancelou', multiple= 'stack', palette=["red", "blue"])
plt.show()

grafico = sns.histplot(data= tabela, x= 'duracao_contrato', hue='cancelou', multiple= 'stack', palette=["red", "blue"])
plt.show()

tabela = tabela[tabela["ligacoes_callcenter"]<=4]
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["dias_atraso"]<=20]
print(tabela["cancelou"].value_counts(normalize=True))

tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
print(tabela["cancelou"].value_counts(normalize=True))