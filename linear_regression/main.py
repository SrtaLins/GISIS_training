import functions

import numpy as np
import matplotlib.pyplot as plt

""" 
Linspace é uma função da biblioteca numpy que está gerando uma
matriz de 101 pontos, espaçados entre -2 e 2.
""" 
x = np.linspace(-2,2,101)

a0 = -2
a1 = -1

y = functions.reta(a0, a1, x)
yn = functions.ruido(y)

# Plotando a reta com o ruído
# functions.plot_reta(x,yn)

mat = functions.solution_space(x,y)

# índicie dos melhores coeficientes:
a0_ind, a1_ind = np.where(mat == np.min(mat))

print(a0_ind, a1_ind)

plt.imshow(mat, extent = [-500,500,-500,500])
plt.scatter([400], [250], c='red', marker='o')
plt.show()
