import numpy as np

import matplotlib.pyplot as plt

domain = int(1e6)

t = np.linspace(-np.pi, np.pi, domain)

a0 = 2*np.sinh(np.pi)/np.pi

signal = a0+np.zeros(domain)

rf = np.exp(-t)

for n in range(1, 500):
    an = a0*((-1)**n / (1 + n**2))
    bn = an*n
    signal += an*np.cos(n*t) - bn*np.sin(n*t)

# Plotagem do Gráfico

xloc = np.linspace(-np.pi, np.pi, 9)

xlab = [r"${}$".format(sym) for sym in (["-\pi", "-\dfrac{3\pi}{4}", "-\dfrac{\pi}{2}", "-\dfrac{\pi}{4}", "0",
                                        "\dfrac{\pi}{4}", "\dfrac{\pi}{2}", "\dfrac{3\pi}{4}", "\pi"])]

fig, ax = plt.subplots(num="Fourier Series - 1º Exemple", figsize=(16, 5))

ax.plot(t, signal - np.pi, label="Fourier Serie")
ax.plot(t, rf, "--", label="Real Function")

ax.set_xlim([-np.pi, np.pi])
ax.set_xticks(xloc)
ax.set_xticklabels(xlab)
ax.legend(loc="upper center", fontsize=15)  # Localização e tamanho das legendas

fig.tight_layout()

plt.show()
