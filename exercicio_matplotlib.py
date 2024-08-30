import matplotlib.pyplot as plt
import pandas as pd

dicionario_de_dados = {
        'nome': ['joao', 'tiago', 'pedro', 'maria', 'ana', 'julia', 'eduarda', 'kaio'],
        'função':['analista de sistemas', 'programador backend', 'cientista de dados', 'pentester', 'pentester', 'cientista de dados', 'analista de sistemas', 'programador backend'],
        'salario': [8000, 7000, 5500, 7200, 4500, 8200, 6870, 5600],
        'horas': [40, 36, 40, 30, 44, 32, 36, 40],
        'experiencia': [10, 8, 5, 6, 6, 4, 7, 3],
        'idade': [35, 32, 30, 36, 32, 28, 40, 29]
    }
dados = pd.DataFrame(dicionario_de_dados)
grafico = dados['salario'].plot.hist()
print(grafico)
plt.show()