import pandas as pd
dic = {
    'nome': ['lucas', 'joao', 'maria', 'jose'],
    'vedas': [1500, 2000, 1700, 2200],
    'comissao': [0.05, 0.07, 0.04, 0.08]
    }
dic_dados = pd.DataFrame(dic)
print(dic_dados)
print(dic_dados.isnull().sum())
print(dic_dados[dic_dados['vedas']>1700])
print(dic_dados.vedas)