import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

base = pd.read_excel("01 - 1. Explicando o projeto.xlsx")
x = base["Data"]
y = base["Curtidas"]

fig, ax = plt.subplots()
ax.bar(x, y, edgecolor="red", linewidth=5.0)

plt.show()
