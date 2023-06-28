import matplotlib.pyplot as plt
import numpy as np

# Utiliza el estilo 'bmh' para el gráfico (opcional, puedes cambiarlo a otro estilo si prefieres)
plt.style.use('bmh')

# Crea los datos
x = [1, 2, 4, 7, 9]
y = [1, 2, 1, 2, 1]

# Crea una figura y un objeto de ejes (subplot)
fig, ax = plt.subplots()

# Grafica los puntos (x, y)
ax.plot(x, y)

# Dibuja una línea horizontal en la posición y=0
ax.axhline(y=0, color='#6b6161')

# Dibuja una línea vertical en la posición x=0
ax.axvline(x=0, color='#6b6161')

# Establece los límites de los ejes y los valores de las marcas de los ejes
ax.set(xlim=(-1, 10), xticks=np.arange(0, 10, 0.5),
       ylim=(-1, 10), yticks=np.arange(0, 10, 0.5))

# Muestra el gráfico
plt.show()
