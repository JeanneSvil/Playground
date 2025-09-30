import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df_videos = pd.read_excel("Backend/Python/Analise de Dados/Graficos com Seaborn/videosYT.xlsx")
fig = sns.scatterplot(data= df_videos, x="Nº de Views", y="Nº de Likes", hue="Responsável",
                      style="Responsável", palette=["red", "black"])
plt.show()

