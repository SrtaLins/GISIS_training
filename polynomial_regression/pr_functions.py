
import numpy as np
# Numpy é uma biblioteca usada para trabalhar com matrizes e vetores.
# O "as np" é um novo nome para a função, para facilitar na hora de utilizar.

def build_polynomial_function(parameters, x): # Contrói a função polinomial	

	polynom = np.zeros_like(x) # Constrói uma matriz de zeros que servirá de base para acumular os polinômios
	
	for k, p in enumerate(parameters):		
		polynom += p*x**k	
	
	return polynom  

def add_noise(data, noise_amplitude):
	return data + noise_amplitude*(0.5 - np.random.rand(len(data)))

def least_squares_solution(x, order, d):

	G = np.zeros((len(d), order))
	
	for k in range(order): 
		G[:,k] = x**k

	GTG = G.T @ G
	GTd = G.T @ d

	return np.linalg.solve(GTG, GTd) 
