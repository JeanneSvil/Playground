import pandas as pd

tabela = pd.read_excel("Backend/Python/Análise de Dados/1- Introdução com Python\Vendas.xlsx")
print(tabela)

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
print(faturamento_por_loja)

faturamento_por_produto = tabela[["ID Loja","Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
print(faturamento_por_produto)