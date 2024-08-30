import pandas as pd
mostra_planilha = pd.read_excel('dados-estudos.xlsx')

#para mostrar a planilha:
print(mostra_planilha)

#para mostra apenas os primeiros itens:
print(mostra_planilha.head(3))

#para mostrar o tipo
print(mostra_planilha.dtypes)

#para dar mais informações
print(mostra_planilha.info())

#para filtrar apenas uma coluna:
print(mostra_planilha['produto'])

#para mostrar apenas uma coluna e ainda ter outro filtro com verdadeiro ou falso
print(mostra_planilha['estoque']>200)

#para mostrar apenas uma coluna e exibir apenas os itens especificos do filtro
print(mostra_planilha[mostra_planilha['estoque']>200])

#para fazer um grafico
print(mostra_planilha.plot.scatter(x='produto', y='vendas'))

#para fazer uma media
print(mostra_planilha['preco'].mean())

print(mostra_planilha.preco.plot())