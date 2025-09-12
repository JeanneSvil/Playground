import plotly.express as px

dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]

fig = px.scatter(x= dados_x, y= dados_y, height= 400, width= 600)
fig.show(renderer= "browser")