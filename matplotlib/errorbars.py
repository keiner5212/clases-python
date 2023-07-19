import matplotlib.pyplot as plt
import numpy as np

# Crear listas con los valores de x, y y error
x = ["xd", "xd1", "xd2", "xd3", "xd4", "xd5", "xd6", "xd7"]
y = [2.390, 2.364, 2.380, 2.390, 2.389, 2.4, 2.4, 2.390]
error = [0.018, 0.0028, 0.003, 0.002, 0.017, 0.02, 0.021, 0.024]

# Crear una lista con los colores para cada punto
colors = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f"
]

# Crear una figura de tamaño 8x5
fig = plt.figure(figsize=[8, 5])

# Agregar un subplot a la figura
ax2 = fig.add_subplot(1, 1, 1)

# Iterar sobre los valores de x
for i in range(len(x)):
    # Crear un gráfico de error para cada punto
    ax2.errorbar(x[i], y[i], yerr=error[i], fmt="D", ecolor=colors[i],
                 color=colors[i], capsize=5, capthick=1, elinewidth=2)

# Establecer los límites del eje y y las marcas del eje y
ax2.set(ylim=[2.3, 2.5], yticks=np.arange(
    2.3, 2.5, 0.05))
# Agregar una cuadrícula al gráfico
ax2.grid(True)

# Mostrar el gráfico
plt.show()
