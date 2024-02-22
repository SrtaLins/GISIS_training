
import numpy as np
# Numpy é uma biblioteca usada para trabalhar com matrizes e vetores. O "as np" é um novo nome para a função, para facilitar na hora de utilizar.
import matplotlib.pyplot as plt
# Matplotlib é uma biblioteca de visualização gráfica, já o pyplot é um módulo da biblioteca que é usado para criação de gráficos.

"""
Passo a passo:
"""
# 1 - Função que descreve a reta
def reta(a0, a1, x):
    y = a0 + a1*x
    return y

# 2 - Aplicar o ruído no eixo y
def ruido(y):
    y_n = y + np.random.rand(len(y))
    return y_n

# 2.1 - Visualização da reta
def plot_reta(x,y):
    fig, ax = plt.subplots()
    ax.plot(x,y)

    fig.tight_layout()
    plt.show()

# 3 - Criar espaço solução com vários coeficientes A0 e A1

# 4 - correlacionar através da norma L2 o dado
def solution_space(x,y):
	
	n = 1001
	
	a0 = np.linspace(-4,4,n)
	a1 = np.linspace(-5,5,n)
	
	a0, a1 = np.meshgrid(a0,a1)
	
	mat = np.zeros((n,n))
	
	for i in range(n):
		for j in range(n):	
			y_p = a0[i,j] + a1[i,j]*x	
	
			mat[i,j] = np.sqrt(np.sum((y - y_p)**2))
		
	return mat

#  5 - Plotar o espaço solução

