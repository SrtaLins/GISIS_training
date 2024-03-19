import numpy as np

import matplotlib.pyplot as plt

domain = int(1e6)

t = np.linspace(-np.pi, np.pi, domain)

a = (2 * np.pi ** 2 ) / 3

rf = (-t ** 2) + 10

signal = a + np.zeros(domain)

for n in range(1, 500):
    b = (4 * (-1) ** (n+1)) / n ** 2
    signal += (b * np.cos(n * t))

#plot
xloc = np.linspace(-np.pi, np.pi, 9)
xlab = [r"${}$".format(sym) for sym in (["-\pi", "-\dfrac{3\pi}{4}", "-\dfrac{\pi}{2}", "-\dfrac{\pi}{4}", "0",
                                        "\dfrac{\pi}{4}", "\dfrac{\pi}{2}", "\dfrac{3\pi}{4}", "\pi"])]

fig, ax = plt.subplots(num="Fourier Series = Exemplo 3", figsize=(13, 5))

ax.plot(t, signal, label="Fourier Series")
ax.plot(t, rf, "--", label="Real Function")
ax.set_xlim(-np.pi, np.pi)
ax.set_xticks(xloc)
ax.set_xticklabels(xlab)
ax.legend(loc="upper right", fontsize=15)

fig.tight_layout()

plt.show()
