import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_videos = pd.read_excel("Backend/Python/Analise de Dados/Graficos com Seaborn/videosYT.xlsx")
grafico_rel = sns.relplot(data=df_videos, x="Nº de Views", y="Nº de Likes", hue="Categoria",
                          col="Responsável", )
grafico_rel.set_titles("Responsável: {col_name}")

plt.show()