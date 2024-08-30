import matplotlib.pyplot as plt


x = {'nome': ['ze', 'chico', 'sebastiao', 'clovi', 'bento']}
y = {'idade': [50, 52, 60, 49, 61]}

fig, ax = plt.subplots()

ax.bar(x['nome'], y['idade'], width=1, edgecolor='white')
plt.show()