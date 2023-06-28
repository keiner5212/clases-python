import matplotlib.pyplot as plt
import numpy as np

# Generar puntos en el eje x
x = np.linspace(0, 10, 50)

# Generar puntos en el eje y
# Utilizamos la función np.random.normal para generar números aleatorios con una distribución normal
# Parámetros de np.random.normal:
#   - Media: 0
#   - Desviación estándar: 50
#   - Tamaño: 50 (generamos 50 puntos)
y = sorted(np.random.normal(0, 50, 50).tolist(), reverse=False)

# Crear una segunda serie de puntos en el eje y (y2) simplemente sumando 1 a cada punto en x
y2 = x + 1

# Crear una figura para el gráfico
fig = plt.figure()

# Añadir un subplot al gráfico (1 fila, 1 columna, índice 1)
ax1 = fig.add_subplot(1, 1, 1)

# Añadir un subplot adicional al gráfico (2 filas, 2 columnas, índice 4)
ax2 = fig.add_subplot(2, 2, 4)

# Graficar los puntos (x, y) en el primer subplot
ax1.plot(x, y, label="ejemplo1")
ax1.set_ylabel("Eje 1")

# Graficar los puntos (x, y2) en el segundo subplot
ax2.plot(x, y2, label="ejemplo2")
ax2.set_ylabel("Eje 2")

# Mostrar una leyenda en ambos subplots
ax1.legend()
ax2.legend()

# Mostrar el gráfico
plt.show()
