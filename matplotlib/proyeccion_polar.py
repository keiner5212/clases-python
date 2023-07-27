# Importa las bibliotecas matplotlib.pyplot y numpy
import matplotlib.pyplot as plt
import numpy as np

# Crea un array de 100 valores equiespaciados entre 0 y 2*pi
theta = np.linspace(0, 2*np.pi, 100)

# Calcula el seno y el coseno de cada valor en el array theta
r1 = np.sin(theta)
r2 = np.cos(theta)

# Crea una gráfica polar con los valores de theta y r1 y r2
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r1, label="seno")
ax.plot(theta, r2, label="coseno")

# Establece el título y la leyenda de la gráfica
ax.set_title("Gráfica polar de seno y coseno")
ax.legend()

# Muestra la gráfica en pantalla
plt.show()
