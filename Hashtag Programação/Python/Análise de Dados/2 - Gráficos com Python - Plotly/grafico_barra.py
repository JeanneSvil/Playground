import plotly.express as px

dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]

graf_coluna = px.bar(x= dados_x, y= dados_y, height= 400, width= 600)
graf_coluna.show(renderer= "browser")