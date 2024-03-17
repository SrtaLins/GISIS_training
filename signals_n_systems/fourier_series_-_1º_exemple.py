import numpy as np
# para trabalhar com matrizes

import matplotlib.pyplot as plt
# para gerar os gráficos, e o módulo pyplot para gerar os gráficos de forma similar ao matlab

# Comece definindo as variáveis:
domain = int(1e6)
"""
essa variável vai indicar a quantidade de pontos no intervalo de tempo. é utilizado um valor
alto (nesse caso 1.000.000) para uma representação mais precisa da função.
Importante: Isso é essencial quando se trabalha com equações mais complexas como transformada
e série de fourrier.
"""

t = np.linspace(-np.pi, np.pi, domain)
""" 
usamos o linspace para montar um espaço vetorial. o np é como estamos chamando o a biblioteca
numpy.
Os itens do linspace são (start, end, tamanho)
O tamanho é quantos elementos terá o array.
No nosso o array vai de -pi à pi, com 1.000.000 de elementos.
"""

frequencie = np.array([2, 3, 5])
"""
Array é uma função da numpy que gera vetores. No caso atual estamos preenchendo apenas o
objeto da função, que o vetor [2, 3, 5] que são as frequências em Hertz.
"""

signal = np.zeros(domain)
"""
A função zeros cria uma matriz de zeros do tamanho indicado, nessa caso, com 1e6 números de 
elementos. Utilizaremos essa matriz para adicionar os valores da série.
Dessa forma o espaço de memória já fica reservado.
"""

for f in frequencie:
    signal += np.sin(2*np.pi*f*t)
"""
Será feito um loop passando item da variável frequencie, utilizando o f para realizar essa ação.
signal será preenchida com o módulo do cos da frequencia*tempo em radianos.
a conversão para radianos é feita com a partir da multiplicação do produto do tempo e frequência
por 2*np.pi.
"""

# Agora a plotagem dos dados
xloc = np.linspace(-np.pi, np.pi, 9)
"""
xloc determina quais os pontos do eixo x serão marcados. Para isso usamos a linspace.
Poderiamos utilizar outras funções também. Como array.
"""

xlab = [r"${}$".format(sym) for sym in ["-\pi", "\dfrac{-3\pi}{4}", "\dfrac{-\pi}{2}", "\dfrac{-\pi}{4}",
        "0", "\dfrac{\pi}{4}", "\dfrac{\pi}{2}", "\dfrac{3\pi}{4}", "\pi"]]
"""
xlab determina qual o rótulos dos pontos do eixos x, que definimos com o xloc.
Utilizamos o r"${}$" para aplicar a notação LaTex no rótulo. Esse linha também poderia ser escrita como:
    xlab = [r"$-\pi$", r"$\dfrac{-3\pi}{4}$", r"$\dfrac{-\pi}{2}$", r"$\dfrac{-\pi}{4}$", 
            r"$0$", r"$\dfrac{\pi}{4}$", r"$\dfrac{\pi}{2}$", r"$\dfrac{3\pi}{4}$", r"$-\pi$"]
o fomart(sym) foi inserido para que não seja necessário repetir o r"${}$" em todos os elementos.


"""

fig, ax = plt.subplots(num="Simple signal", figsize=(15, 5))

ax.plot(t, signal)

ax.set_xticks(xloc)
ax.set_xticklabels(xlab)
ax.set_xlim([-np.pi, np.pi])
ax.set_xlabel("t [s]", fontsize=15)
ax.set_ylabel("Amplitude", fontsize=15)

fig.tight_layout()
plt.show()
