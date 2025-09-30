import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_videos = pd.read_excel("Backend/Python/Analise de Dados/Graficos com Seaborn/videosYT.xlsx")
graf_regre = sns.regplot(data=df_videos, x="Nº de Views", y="Nº de Likes")
plt.show()

graf_regre = sns.lmplot(data=df_videos, x="Nº de Views", y="Nº de Likes", hue= "Responsável",
                        markers= ['o', 'x'])
plt.show()