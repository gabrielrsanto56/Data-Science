#importe a biblioteca pandas para tratar os dados
import pandas as pd

import matplotlib.pyplot as plt

#atribua uma variavel para receber os dados
conteudo = pd.read_excel('01 - 1. Explicando o projeto.xlsx')


#como as informações da coluna "Visualizações" não são relevantes podemos apaga-la
conteudo = conteudo.drop('Visualizações', axis=1)

print(conteudo.head())
print(conteudo.tail())
print(conteudo.info())

#como na coluna carrossel tem apenas 8 valores não nulos temos que trata-la
print(conteudo.Carrossel.value_counts())

#mostrando quais linhas da coluna carrossel nao sao nulas e nao nulas
print(conteudo.loc[conteudo.Carrossel.notnull()].head(10))


#atribuindo a netra N para espaços nulos em carrossel
conteudo.loc[conteudo.Carrossel.isnull(), 'Carrossel'] = 'N'

#analisando um resumo estatistico sobre os dados
print(conteudo.describe())

#vendo quais fotos tiveram mais  e menos curtidas
print(conteudo.sort_values(by="Curtidas", ascending=False).head())
print('')
print(conteudo.sort_values(by="Curtidas", ascending=False).tail())

#analisando quais conteudos mais têm engajamento
print(conteudo.groupby("Tipo")[["Curtidas", "Comentários"]].mean())
print('')
print(conteudo.groupby("Pessoas")[["Curtidas", "Comentários"]].mean())
print('')
print(conteudo.groupby("Campanhas")[["Curtidas", "Comentários"]].mean())
print('')
print(conteudo[conteudo.Tipo =="Foto"].groupby("Carrossel")[["Curtidas", "Comentários"]].mean())
print('')

#separando conteudos com mais de uma tag
conteudo.Tags = conteudo.Tags.str.split("/")
conteudo = conteudo.explode("Tags")
conteudo.loc[conteudo.Tags.isnull(), "Tags"] = "Sem Tag"
print(conteudo.groupby("Tags")[["Curtidas", "Comentários"]].mean().sort_values(by="Curtidas",ascending=False))
