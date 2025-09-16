import pandas as pd
import plotly.express as px

tarefas = pd.read_excel('Tarefas.xlsx')
fig = px.timeline(tarefas, x_start= "Início", x_end= "Fim", y= "Tarefa")
fig.update_yaxes(autorange= 'reversed')
fig.show(renderer= "browser")