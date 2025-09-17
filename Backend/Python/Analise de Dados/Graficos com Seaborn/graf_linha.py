import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_incritos = pd.read_excel('Backend/Python/Analise de Dados/Graficos com Seaborn/videosYT.xlsx', 'Inscritos')
graf_linha = sns.lineplot(data= df_incritos, x= 'Mês/Ano', y='Inscritos', color= 'red')
plt.show()