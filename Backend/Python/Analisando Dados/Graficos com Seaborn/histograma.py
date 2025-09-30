import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_videos = pd.read_excel("Backend/Python/Analise de Dados/Graficos com Seaborn/videosYT.xlsx")
fig = sns.displot(data=df_videos, x="Nº de Views")
plt.show()

fig = sns.displot(data=df_videos, x="Nº de Views", kind= 'kde')
plt.show()

fig = sns.displot(data=df_videos, x="Nº de Views", kind= 'ecdf')
plt.show()

fig = sns.displot(data=df_videos, x="Nº de Views", hue= "Responsável", col= "Responsável", rug= True)
plt.show()

fig = sns.pairplot(data=df_videos,hue= "Responsável")
plt.show()