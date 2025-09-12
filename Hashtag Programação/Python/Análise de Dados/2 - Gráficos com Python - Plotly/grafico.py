import plotly.express as px

dados_x = ['2018', '2019', '2020', '2021']
dados_y = [10, 20, 5, 35]

fig = px.line(x= dados_x, y=dados_y, title= "Vendas x Ano", width= 600, height= 300, line_shape='spline')
fig.update_yaxes(title= 'Vendas', title_font_color= 'blue', ticks='outside', tickfont_color='yellow')
fig.update_xaxes(title= 'Ano', title_font_color='red', ticks='outside', tickfont_color='yellow')
fig.update_layout(paper_bgcolor='black', plot_bgcolor='black', font_color='white', 
                  font_family='arial', font_lineposition='under', font_shadow='auto', 
                  font_size= 12, font_weight= 600)

fig.show(renderer= "browser")