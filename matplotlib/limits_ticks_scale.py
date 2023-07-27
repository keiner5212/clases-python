# Importa la biblioteca matplotlib.pyplot
import matplotlib.pyplot as plt

# Crea una gráfica con algunos datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)

# Establece los límites de los ejes x e y
plt.xlim(0, 6)
plt.ylim(0, 12)

# Establece los ticks de los ejes x e y
plt.grid(True)
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([2, 4, 6, 8, 10])

# Establece la escala de los ejes x e y
plt.xscale('linear')
plt.yscale('linear')

"""
linear: Escala lineal.
log: Escala logarítmica.
symlog: Escala logarítmica simétrica.
logit: Escala logística.
function: Escala personalizada definida por una función.
"""

# Muestra la gráfica en pantalla
plt.show()
